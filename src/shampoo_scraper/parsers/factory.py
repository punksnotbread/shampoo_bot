from .base import Parser
from .camelia import CameliaParser
from .eurovaistine import EurovaistineParser
from .gintarinevaistine import GintarinevaistineParser


def make_parser(type: str) -> Parser:
    if type == "camelia":
        return CameliaParser()
    elif type == "eurovaistine":
        return EurovaistineParser()
    elif type == "gintarinevaistine":
        return GintarinevaistineParser()

    raise ValueError(f"Type {type} is not supported!")
