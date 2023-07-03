from .base import URLBuilder


class GintarinevaistineURLBuilder(URLBuilder):
    def __init__(self):
        super().__init__()
        self._search_url = "https://www.gintarine.lt/search?q="
