from abc import ABC, abstractmethod

from lxml import etree


class Parser(ABC):
    def __init__(self):
        self._parser = etree.HTMLParser()

    @abstractmethod
    def parse(self, body: str) -> dict[str, str]:
        """Parse document for product information."""
