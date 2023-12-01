import os

import aiofiles
import bcrypt
import core.config as config
from core.exception import (
    ImgFileExtensionException,
    ImgUploadException,
    InvalidPasswordException,
    NoProfileImgException,
    PasswordsEqualException,
)
from data.user_table import DBUser, UserDB
from fastapi import UploadFile
from fastapi.responses import FileResponse
from model.user import User
from service.login import LoginService

app_config = config.get_config()
user_db = UserDB()
login_service = LoginService()


class UserService:
    def get_user_info(self, user: User):
        return user

    async def change_password(
        self, user: DBUser, old_password: str, new_password: str
    ) -> FileResponse:
        if not login_service.verify_password(old_password, user.hashed_password):
            raise InvalidPasswordException()

        if old_password == new_password:
            raise PasswordsEqualException()

        new_hashed_password = bcrypt.hashpw(
            new_password.encode(), bcrypt.gensalt()
        ).decode()
        await user_db.change_password(user.username, new_hashed_password)

        return "ok"

    def get_user_profile_img(self, user: User) -> FileResponse:
        profile_img_path = os.path.join(
            app_config.WEBROOT_PATH, "img", user.username, "profile.png"
        )

        if os.path.exists(profile_img_path) and os.path.isfile(profile_img_path):
            return FileResponse(profile_img_path)
        else:
            raise NoProfileImgException()

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
