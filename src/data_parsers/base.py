from abc import abstractmethod
from io import BytesIO

from src.dto.file_data import FileData


class BaseParser:
    """
    Abstract class for parsing config file
    """

    @abstractmethod
    def parse(self, file_data: BytesIO) -> FileData:
        """
        Parses the file and returns information about the current battle
        Parameters:
            file_data (BytesIO): path to config file
        Returns:
            FileData: Info by current battle
        """
