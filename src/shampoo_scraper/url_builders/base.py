from abc import ABC


class URLBuilder(ABC):
    def __init__(self):
        self._search_url = None

    def build(self, input: str) -> str:
        if self._search_url is None:
            raise ValueError("No search url prefix provided.")

        return self._search_url + "+".join(input.split(" "))
