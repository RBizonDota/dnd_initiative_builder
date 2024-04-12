from prettytable import PrettyTable

from src.builders.base import BaseIniBuilder


class DynamicIniBuilder(BaseIniBuilder):

    def build(self):
        table = PrettyTable(["Номер", "Имя персонажа", "Игрок", "Ини"])
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
        i = 1
        for char_name, username, roll, _ in chars:
            table.add_row([i, char_name, username or "", roll])
            i += 1

        print(table)
