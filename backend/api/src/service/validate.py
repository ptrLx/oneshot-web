from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import data.user_db as user_db
from jose import JWTError, jwt
from typing import Annotated
from model.token import TokenData
from model.user import User
from core.config import SECRET_KEY, ALGORITHM


__oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def __get_current_user(token: Annotated[str, Depends(__oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_db.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(__get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user