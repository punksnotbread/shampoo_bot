from .base import URLBuilder


class CameliaURLBuilder(URLBuilder):
    def __init__(self):
        super().__init__()
        self._search_url = "https://camelia.lt/jolisearch?s="
