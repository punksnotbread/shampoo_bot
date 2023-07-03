from .base import URLBuilder


class EurovaistineURLBuilder(URLBuilder):
    def __init__(self):
        super().__init__()
        self._search_url = "https://www.eurovaistine.lt/paieska/rezultatai?q="
