from enum import Enum

from pydantic import BaseModel, validator


class UserRoleDTO(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class UserDTO(BaseModel):
    username: str
    role: UserRoleDTO
    disabled: bool
    full_name: str | None = None

    @validator("username")
    def validate_username_format(cls, v: str):
        return v.lower()
