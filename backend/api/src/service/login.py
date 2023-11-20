from datetime import datetime, timedelta

import core.config as config
from data.user_db import UserDB
from fastapi import HTTPException, status
from jose import jwt
from model.token import Token
from passlib.context import CryptContext

app_config = config.get_config()
user_db = UserDB()


class LoginService:
    def __init__(self) -> None:
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __verify_password(self, plain_password, hashed_password) -> bool:
        return self.__pwd_context.verify(plain_password, hashed_password)

    async def __authenticate_user(self, username: str, password: str):
        user = await user_db.get_user(username)
        if not user:
            return False
        if not self.__verify_password(password, user.hashed_password):
            return False
        return user

    def __create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, app_config.SECRET_KEY, algorithm=app_config.ALGORITHM
        )
        return encoded_jwt

    # def get_password_hash(self, password):
    #     return self.__pwd_context.hash(password)

    async def login_user(self, username: str, password: str) -> Token:
        user = await self.__authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=app_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
