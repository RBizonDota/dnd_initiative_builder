from abc import abstractmethod
from random import randint

from src.dto.file_data import FileData, IniMode


class BaseIniBuilder:
    def __init__(self, data: FileData):
        self._config = data.config
        self._characters = data.characters
        self._enemies = data.enemies

    @abstractmethod
    def build(self): ...

    def roll(self, bonus: int, mod: IniMode) -> int:
        if mod == IniMode.STRAIGHT:
            return randint(1, 20) + bonus
        elif mod == IniMode.ADVANTAGE:
            return max(randint(1, 20), randint(1, 20)) + bonus
        elif mod == IniMode.DISADVANTAGE:
            return min(randint(1, 20), randint(1, 20)) + bonus
        raise ValueError(f"Invalid mod value: {mod}")
