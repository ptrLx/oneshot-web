import os
from typing import Annotated

import aiofiles
import core.config as config
from core.exeption import ImgFileExtensionException, ImgUploadException, NoProfileImg
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse
from model.user import User
from service.user import UserService
from service.validate import get_current_active_user

router = APIRouter()

user_service = UserService()

app_config = config.get_config()


@router.get("/me")
async def get_user_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
    return user_service.get_user_info(current_user)


@router.get("/profileimg")
async def get_user_profile_img(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> FileResponse:
    profile_img_path = os.path.join(
        app_config.WEBROOT_PATH, "img", current_user.username, "profile.png"
    )

    if os.path.exists(profile_img_path) and os.path.isfile(profile_img_path):
        return FileResponse(profile_img_path)
    else:
        raise NoProfileImg


@router.post("/profileimg")
async def upload_user_profile_img(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile = File(...),
) -> str:
    profile_img_path = os.path.join(
        app_config.WEBROOT_PATH, "img", current_user.username, "profile.png"
    )
    file_extension = (
        file.filename[file.filename.rfind(".") + 1 :] if "." in file.filename else None
    )
    if file_extension != "png":
        raise ImgFileExtensionException

    try:
        async with aiofiles.open(profile_img_path, "wb") as f:
            # todo ensure file size is small
            while contents := await file.read(app_config.MAX_FILE_UPLOAD_CHUNK_SIZE_B):
                await f.write(contents)
    except Exception:
        raise ImgUploadException
    finally:
        await file.close()

    return "ok"


@router.post("/chpw")
async def change_user_password(
    old_password,
    new_password,
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> str:
    return user_service.change_password(old_password, new_password, current_user)
