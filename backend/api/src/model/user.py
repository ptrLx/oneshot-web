from enum import Enum

from pydantic import BaseModel, validator


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class User(BaseModel):
    username: str
    role: UserRole
    disabled: bool
    full_name: str | None = None

    @validator("username")
    def validate_username_format(cls, v: str):
        return v.lower()
