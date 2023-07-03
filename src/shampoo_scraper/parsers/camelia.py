import logging

from lxml import etree

from .base import Parser

logger = logging.getLogger(f"{__name__}")


class CameliaParser(Parser):
    def __init__(self):
        super().__init__()
        self._base_url = "https://camelia.lt/"
        self._type = "Camelia"

    def _parse_url(self, el: etree.Element) -> str:
        xpath = ".//@href"
        url = el.xpath(xpath)
        if url:
            return url[0]

        return ""

    def _parse_title(self, el: etree.Element) -> str:
        xpath = ".//*[@class='product-name ']/a/@title"
        title = el.xpath(xpath)
        if title:
            return title[0]

        return ""

    def _parse_price(self, el: etree.Element) -> str:
        xpath = ".//span[contains(@class, 'price')]/text()"
        price = el.xpath(xpath)
        if price:
            return price[0].strip()

        return ""

    def _parse_discounted_price(self, el: etree.Element) -> str:
        xpath = ".//div[contains(@class, 'cm-club-price-list')]/div/text()"
        price = el.xpath(xpath)
        if price:
            return price[0].strip()

        return ""

    def parse(self, body: str) -> list[dict[str, str]]:
        tree = etree.HTML(body)
        products = tree.xpath(".//div[@class='product-container']")
        logger.debug(f"Found {len(products)} products in page.")

        results = []

        for product in products:
            try:
                results.append(
                    {
                        "url": self._parse_url(product),
                        "title": self._parse_title(product),
                        "price": self._parse_price(product),
                        "discounted_price": self._parse_discounted_price(product),
                        "type": self._type,
                    }
                )
            except Exception as e:
                logger.error(f"Exception when parsing product: {e}")

        return results
