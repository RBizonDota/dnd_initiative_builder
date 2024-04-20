# pylint: skip-file
import re
import typing

from pydantic import BaseModel, Field, field_validator

from src.dto.enums import IniMode

mod_template = r"(\d)d(\d)|(\d)к(\d)"


class IniMember(BaseModel):
    bonus: int
    mod: IniMode | None = Field(default=IniMode.STRAIGHT)
    user: str | None = None
    bonus_roll: list[tuple[int, int]] = []

    @field_validator("bonus_roll", mode="before")
    def parse_bonus(cls, v: typing.Any) -> list[tuple[str, str]]:
        if isinstance(v, str):
            return [
                (i[0], i[1]) if all((i[0], i[1])) else (i[2], i[3])
                for i in re.findall(mod_template, v)
            ]
        return v


class IniConfig(BaseModel):
    pass


class FileData(BaseModel):
    characters: dict[str, IniMember]
    enemies: dict[str, IniMember]
    config: IniConfig | None = None
