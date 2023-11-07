from typing import Annotated

import aiofiles
from core import config
from core.exeption import ImgFileExtensionException, ImgUploadException
from fastapi import APIRouter, Depends, File, UploadFile
from model.oneshot import OneShot
from model.user import User
from service.validate import get_current_active_user

router = APIRouter()


app_config = config.get_config()


@router.post("/upload")
async def upload_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    oneshot: OneShot = Depends(),
    file: UploadFile = File(...),
):
    file_extension = (
        file.filename[file.filename.rfind(".") + 1 :] if "." in file.filename else None
    )
    if file_extension not in app_config.ONESHOT_ALLOWED_FILE_EXTENSIONS:
        raise ImgFileExtensionException

    file_name = f"{oneshot.get_file_name()}.{file_extension}"

    path = f"{app_config.WEBROOT_PATH}/img/{current_user.username}/{file_name}"
    try:
        async with aiofiles.open(path, "wb") as f:
            # todo use max file size
            while contents := await file.read(app_config.MAX_FILE_UPLOAD_CHUNK_SIZE_B):
                await f.write(contents)

    except Exception:
        raise ImgUploadException
    finally:
        await file.close()

    # todo create preview
    # todo store in db

    return "ok"
