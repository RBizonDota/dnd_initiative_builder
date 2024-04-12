from abc import abstractmethod
from io import BytesIO

from src.dto.file_data import FileData


class BaseParser:
    @abstractmethod
    def parse(self, file_data: BytesIO) -> FileData: ...
