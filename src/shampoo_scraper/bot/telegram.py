import logging

import httpx

from .base import Bot

logger = logging.getLogger(f"{__name__}")


class TelegramBot(Bot):
    async def send(self, msg: str) -> None:
        url = f"https://api.telegram.org/bot{self._token}/sendMessage"
        httpx.Timeout(connect=5, read=None, write=5, pool=5)

        response = httpx.post(
            url,
            json={
                "chat_id": self._chat_id,
                "text": msg,
                "no_webpage": False,
                "disable_web_page_preview": True,
            },
        )

        logger.info(response.text)
