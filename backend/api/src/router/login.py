from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from model.token import Token

from service.login import LoginService

router = APIRouter()

login_service = LoginService()


@router.post("/", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return login_service.login_user(form_data.username, form_data.password)
