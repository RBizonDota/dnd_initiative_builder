# pylint: skip-file
from pydantic import BaseModel, Field

from src.dto.enums import IniMode


class IniMember(BaseModel):
    bonus: int
    mod: IniMode | None = Field(default=IniMode.STRAIGHT)
    user: str | None = None


class IniConfig(BaseModel):
    pass


class FileData(BaseModel):
    characters: dict[str, IniMember]
    enemies: dict[str, IniMember]
    config: IniConfig | None = None
