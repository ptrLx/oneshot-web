import os

import aiofiles
from core import config
from core.exception import (
    ImgFileExtensionException,
    ImgUploadException,
    NoOneShotImgFound,
)
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse
from model.date import Date
from model.oneshot import OneShot, OneShotFileName
from model.user import User

app_config = config.get_config()


class ImageService:
    async def store_image(self, user: User, oneshot: OneShot, file: UploadFile) -> str:
        file_extension = (
            file.filename[file.filename.rfind(".") + 1 :].lower()
            if "." in file.filename
            else None
        )

        if file_extension is None:
            raise ImgFileExtensionException()

        file_name = OneShotFileName(
            file_name=oneshot.get_file_name_no_ext(), file_extension=file_extension
        )

        path = os.path.join(
            app_config.WEBROOT_PATH, "img", user.username, file_name.get_file_name()
        )
        try:
            async with aiofiles.open(path, "wb") as f:
                # todo use max file size
                while contents := await file.read(
                    app_config.MAX_FILE_UPLOAD_CHUNK_SIZE_B
                ):
                    await f.write(contents)

        except Exception:
            raise ImgUploadException()
        finally:
            await file.close()

        # todo create preview
        # todo store in db

        return file_name.get_file_name()

    async def download_image_by_date(self, user: User, date: Date) -> FileResponse:
        # todo find file name in db
        from fastapi import HTTPException
        from starlette import status

        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="not implemented"
        )

    async def download_image_by_file_name(
        self, user: User, file_name: OneShotFileName
    ) -> FileResponse:
        img_path = os.path.join(
            app_config.WEBROOT_PATH,
            "img",
            user.username,
            file_name.get_file_name(),
        )

        if os.path.exists(img_path) and os.path.isfile(img_path):
            return FileResponse(img_path)
        else:
            raise NoOneShotImgFound()
