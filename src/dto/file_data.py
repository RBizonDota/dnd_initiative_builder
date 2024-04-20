# pylint: skip-file
import re
import typing

from pydantic import BaseModel, Field, field_validator

from src.dto.enums import IniMode

parse_template = r"(\dd\d)|(\dк\d)"


class IniMember(BaseModel):
    bonus: int
    mod: IniMode | None = Field(default=IniMode.STRAIGHT)
    user: str | None = None
    bonus_roll: tuple[int, ...] = tuple()

    @field_validator("bonus_roll", mode="before")
    def parse_bonus(cls, v: typing.Any) -> typing.Tuple[typing.Any, ...]:
        if isinstance(v, str):
            list_bonus = [i[0] or i[1] for i in re.findall(parse_template, v)]
            return tuple(i[2:] for i in list_bonus)
        return v


class IniConfig(BaseModel):
    pass


class FileData(BaseModel):
    characters: dict[str, IniMember]
    enemies: dict[str, IniMember]
    config: IniConfig | None = None
