import asyncio
import itertools
import json
import logging
import random

from aiolimiter import AsyncLimiter
from playwright.async_api import BrowserContext, async_playwright

from shampoo_scraper.bot import make_bot
from shampoo_scraper.exceptions import ScrapeNotSuccessfulError
from shampoo_scraper.parsers import make_parser
from shampoo_scraper.settings import Settings
from shampoo_scraper.url_builders import make_url_builder

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)
logger = logging.getLogger(f"{__name__}")


def generate_searches(settings: Settings) -> list[tuple[str, str]]:
    # TODO: Make them json in pydantic model.
    return list(
        itertools.product(
            json.loads(settings.SEARCH_TYPES),
            json.loads(settings.QUERIES),
        )
    )


async def goto_page(context: BrowserContext, url: str) -> str:
    logger.debug(f"Starting for {url}")
    page = await context.new_page()
    response = await page.goto(url)

    logger.info(f"Status code: {response.status} for {url}")

    if response.status == 200:
        await asyncio.sleep(3)
    else:
        logger.warning("Status code not 200, not waiting.")
        raise ScrapeNotSuccessfulError

    content = await page.content()
    return content


async def run_process(
    limiter: AsyncLimiter,
    type_: str,
    url: str,
) -> dict[str, str] | None:
    async with limiter:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(
                ignore_https_errors=True,
                color_scheme=random.choice(["dark", "light", "no-preference"]),
                locale="en-US",
                java_script_enabled=True,
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",  # noqa
            )
            try:
                html = await goto_page(context, url)
            except ScrapeNotSuccessfulError:
                logger.info(f"Scrape was not successful for `{url}`, not parsing.")
                return None

        logger.debug(f"Parsing for `{type_}`.")
        parser = make_parser(type_)
        try:
            result = parser.parse(html)
        except Exception as e:
            logger.error(f"Exception when parsing: {e}")
            result = None

        if not result:
            outfn = url.split("/")[-1] + ".html"
            logger.warning(f"No products parsed for `{url}`, saving html to `{outfn}`")
            with open(outfn, "w") as outfile:
                outfile.write(html)

        return result


def format_msg(res: dict) -> str:
    return f"• {res['title']}\n• PRICE: {res['price']}\n• URL: {res['url']}"


async def amain():
    settings = Settings()
    logger.info(f"Configured environment is: `{settings.ENVIRONMENT}`.")

    bot = make_bot("telegram", settings.BOT_TOKEN, settings.CHAT_ID)

    searches = generate_searches(settings)

    limiter = AsyncLimiter(settings.PARALEL_JOB_COUNT, time_period=10)

    tasks = []
    logger.debug(f"Will do {len(searches)} jobs.")
    logger.debug(f"Searches in question: {searches}")
    for type_, search in searches:
        url_builder = make_url_builder(type_)
        url = url_builder.build(search)

        tasks.append(run_process(limiter, type_, url))

    results = await asyncio.gather(*tasks)

    msgs = ""
    for res in results:
        if res is None:
            continue

        logger.debug(f"Formatting messages from result: {res}")
        for product in res:
            msgs += format_msg(product) + "\n\n"
        msgs += "\n"

    if settings.ENVIRONMENT == "prod":
        await bot.send(msgs)
    else:
        logger.info(f"Finished msg: {msgs}")

    logger.info("Sequence complete, exiting.")


if __name__ == "__main__":
    asyncio.run(amain())
