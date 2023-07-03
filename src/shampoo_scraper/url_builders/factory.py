from .base import URLBuilder
from .camelia import CameliaURLBuilder
from .eurovaistine import EurovaistineURLBuilder
from .gintarinevaistine import GintarinevaistineURLBuilder


def make_url_builder(type: str) -> URLBuilder:
    if type == "camelia":
        return CameliaURLBuilder()
    elif type == "eurovaistine":
        return EurovaistineURLBuilder()
    elif type == "gintarinevaistine":
        return GintarinevaistineURLBuilder()

    raise ValueError(f"Type {type} is not supported!")
