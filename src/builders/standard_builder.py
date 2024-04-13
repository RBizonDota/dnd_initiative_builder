from prettytable import PrettyTable

from src.builders.base import BaseIniBuilder


class DynamicIniBuilder(BaseIniBuilder):
    """
    Class for building a battle table by ini file

    Attributes:
        data (FileData): info about the fight
    """

    def build(self) -> list[tuple[str, str | None, int, int]]:
        chars = [
            *[
                (char_name, char.user, self.roll(char.bonus, char.mod), char.bonus)
                for char_name, char in self._characters.items()
            ],
            *[
                (char_name, char.user, self.roll(char.bonus, char.mod), char.bonus)
                for char_name, char in self._enemies.items()
            ],
        ]
        chars.sort(key=lambda x: x[3], reverse=True)
        chars.sort(key=lambda x: x[2], reverse=True)
        return chars

    def print_table(self):
        table = PrettyTable(["Номер", "Имя персонажа", "Игрок", "Ини"])
        chars = self.build()
        for index, char in enumerate(chars):
            char_name, username, roll, _ = char
            table.add_row([index + 1, char_name, username or "", roll])
        print(table)
