from abc import ABC, abstractmethod
from random import randint

from src.dto.file_data import FileData, IniMode


class BaseIniBuilder(ABC):
    """
    Abstract class for building a battle table

    Attributes:
        data (FileData): info about the fight
    """

    def __init__(self, data: FileData):
        self._config = data.config
        self._characters = data.characters
        self._enemies = data.enemies

    @abstractmethod
    def build(self) -> list[tuple[str, str | None, int, int]]:
        """
        Builds list with info and initiative all chars
        Returns:
            list[tuple[str, str | None, int, int]]: list with info and initiative all chars
        """

    @abstractmethod
    def print_table(self):
        """Builds and prints a table about the fight in the console"""

    def roll(self, bonus: int, mod: IniMode) -> int:
        """
        Generate a cube roll for a selected character
        Parameters:
            bonus (int): bonus to the roll of the selected character
            mod (IniMode): mode to the roll of the selected character
        """
        if mod == IniMode.STRAIGHT:
            return randint(1, 20) + bonus
        if mod == IniMode.ADVANTAGE:
            return max(randint(1, 20), randint(1, 20)) + bonus
        if mod == IniMode.DISADVANTAGE:
            return min(randint(1, 20), randint(1, 20)) + bonus
        raise ValueError(f"Invalid mod value: {mod}")
