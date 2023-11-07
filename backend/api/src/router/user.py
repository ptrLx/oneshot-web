import os
from typing import Annotated

import core.config as config
from core.exeption import NoProfileImg
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from model.user import User
from service.user import UserService
from service.validate import get_current_active_user

router = APIRouter()

user_service = UserService()

app_config = config.get_config()


@router.get("/me", response_model=User)
async def get_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return user_service.get_user_info(current_user)


@router.get("/profileimg")
async def get_user_profile_img(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    profile_img_path = (
        f"{app_config.WEBROOT_PATH}/img/{current_user.username}/profile.png"
    )

    if os.path.exists(profile_img_path) and os.path.isfile(profile_img_path):
        return FileResponse(profile_img_path)
    else:
        raise NoProfileImg


@router.post("/chpw")
async def change_user_password(
    old_password,
    new_password,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return user_service.change_password(old_password, new_password, current_user)
