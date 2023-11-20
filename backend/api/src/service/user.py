import os

import aiofiles
import core.config as config
from core.exception import ImgFileExtensionException, ImgUploadException, NoProfileImg
from fastapi import UploadFile
from fastapi.responses import FileResponse
from model.user import User

app_config = config.get_config()


class UserService:
    def get_user_info(self, user: User):
        return user

    def change_password(
        self, user: User, old_password: str, new_password: str
    ) -> FileResponse:
        # todo verify old pw, create new hash, update db
        return "ok"

    def get_user_profile_img(self, user: User) -> FileResponse:
        profile_img_path = os.path.join(
            app_config.WEBROOT_PATH, "img", user.username, "profile.png"
        )

        if os.path.exists(profile_img_path) and os.path.isfile(profile_img_path):
            return FileResponse(profile_img_path)
        else:
            raise NoProfileImg()

    async def upload_user_profile_img(self, user: User, file: UploadFile) -> str:
        profile_img_path = os.path.join(
            app_config.WEBROOT_PATH, "img", user.username, "profile.png"
        )
        file_extension = (
            file.filename[file.filename.rfind(".") + 1 :]
            if "." in file.filename
            else None
        )
        if file_extension != "png":
            raise ImgFileExtensionException()

        try:
            async with aiofiles.open(profile_img_path, "wb") as f:
                # todo ensure file size is small or calculate smaller image
                while contents := await file.read(
                    app_config.MAX_FILE_UPLOAD_CHUNK_SIZE_B
                ):
                    await f.write(contents)
        except Exception:
            raise ImgUploadException()
        finally:
            await file.close()

        return "ok"
