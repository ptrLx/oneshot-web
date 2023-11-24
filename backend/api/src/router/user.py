from typing import Annotated

from data.user_table import DBUser
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse
from model.user import User
from service.user import UserService
from service.validate import get_current_active_user

router = APIRouter()

user_service = UserService()


@router.get("/me")
async def get_user_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
    return user_service.get_user_info(current_user)


@router.get("/profileimg")
async def get_user_profile_img(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> FileResponse:
    return user_service.get_user_profile_img(current_user)


@router.post("/profileimg")
async def upload_user_profile_img(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile = File(...),
) -> str:
    return await user_service.upload_user_profile_img(current_user, file)


@router.post("/chpw")
async def change_user_password(
    current_user: Annotated[DBUser, Depends(get_current_active_user)],
    old_password,
    new_password,
) -> str:
    return await user_service.change_password(current_user, old_password, new_password)
