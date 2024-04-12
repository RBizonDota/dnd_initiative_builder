from io import BytesIO

import yaml
from yaml.loader import SafeLoader

from src.data_parsers.base import BaseParser
from src.dto.file_data import FileData


class YamlParser(BaseParser):
    def parse(self, file_data: BytesIO) -> FileData:
        data = FileData(**yaml.load(file_data, Loader=SafeLoader))
        return data
