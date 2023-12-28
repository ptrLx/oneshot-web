from datetime import datetime
from typing import Annotated

import core.config as config
from core.exception import CredentialValidationException
from data.user_table import DBUser, UserDB
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from model.token import TokenDataDTO
from model.user import UserDTO

__oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/")

app_config = config.get_config()
user_db = UserDB()


async def __get_current_user(token: Annotated[str, Depends(__oauth2_scheme)]) -> DBUser:
    try:
        payload = jwt.decode(
            token, app_config.SECRET_KEY, algorithms=[app_config.ALGORITHM]
        )
        token_data = TokenDataDTO(username=payload.get("sub"), exp=payload.get("exp"))
    except:
        raise CredentialValidationException

    if token_data.exp < int(datetime.utcnow().timestamp()):
        raise CredentialValidationException

    user = await user_db.get_user(username=token_data.username)
    if user is None:
        raise CredentialValidationException
    return user


async def get_current_active_user(
    current_user: Annotated[UserDTO, Depends(__get_current_user)]
) -> DBUser:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
