from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class User(BaseModel):
    username: str
    role: UserRole
    disabled: bool
    full_name: str | None = None
    profileimg: str | None = None


class UserInDB(User):
    hashed_password: str
