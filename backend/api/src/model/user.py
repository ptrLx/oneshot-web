from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class User(BaseModel):
    username: str
    role: UserRole
    disabled: bool
    full_name: str | None = None
    # * profileimg is always profile.png
    # // profileimg: str | None = None
