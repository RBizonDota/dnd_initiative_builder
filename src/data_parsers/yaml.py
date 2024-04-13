import yaml
from yaml.loader import SafeLoader

from src.data_parsers.base import BaseParser
from src.dto.file_data import FileData


class YamlParser(BaseParser):
    """
    Class for parsing config ini-file
    """

    def parse(self, filename: str) -> FileData:
        with open(filename, "rb") as f:
            data = FileData(**yaml.load(f, Loader=SafeLoader))
        return data
