from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from model.token import TokenDTO
from service.login import LoginService

router = APIRouter()

login_service = LoginService()


@router.post("/", response_model=TokenDTO)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> TokenDTO:
    return await login_service.login_user(form_data.username, form_data.password)
