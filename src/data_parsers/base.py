from abc import abstractmethod

from src.dto.file_data import FileData


class BaseParser:
    """
    Abstract class for parsing config file
    """

    @abstractmethod
    def parse(self, filename: str) -> FileData:
        """
        Parses the file by path and returns information about the current battle
        Parameters:
            filename (str): path to config file
        Returns:
            FileData: Info by current battle
        """
