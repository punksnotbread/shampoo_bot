from .base import Bot
from .telegram import TelegramBot


def make_bot(type: str, token: str, chat_id: str) -> Bot:
    if type == "telegram":
        return TelegramBot(token, chat_id)

    raise ValueError(f"Type {type} is not supported!")
