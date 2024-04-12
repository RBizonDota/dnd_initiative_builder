from enum import Enum


class IniMode(str, Enum):
    ADVANTAGE = "adv"
    DISADVANTAGE = "dis"
    STRAIGHT = "str"


class ParserEnum(str, Enum):
    YAML = "yaml"

    @classmethod
    def values(cls) -> list[str]:
        return [e.value for e in cls]


class BuilderEnum(str, Enum):
    STANDARD = "std"

    @classmethod
    def values(cls) -> list[str]:
        return [e.value for e in cls]
