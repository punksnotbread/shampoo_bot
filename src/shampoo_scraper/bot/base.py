from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self, token: str, chat_id: str):
        self._token = token
        self._chat_id = chat_id

    @abstractmethod
    async def send(self, msg: str) -> None:
        ...
