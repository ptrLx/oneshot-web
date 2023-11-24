from typing import Annotated

import core.config as config
from data.user_table import DBUser, UserDB
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from model.token import TokenData
from model.user import User

__oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/")

app_config = config.get_config()
user_db = UserDB()


async def __get_current_user(token: Annotated[str, Depends(__oauth2_scheme)]) -> DBUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, app_config.SECRET_KEY, algorithms=[app_config.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await user_db.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(__get_current_user)]
) -> DBUser:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
