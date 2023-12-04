import os

import aiofiles
from core import config
from core.exception import (
    ImgFileExtensionException,
    ImgUploadException,
    InvalidPageSizeException,
    NoOneShotImgFoundException,
    NoOneShotInDBFoundException,
    UnprocessableImageException,
)
from data.oneshot_table import DBOneShot, OneShotDB
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse
from model.date import DateDTO
from model.oneshot import OneShotDTO, OneShotFileNameDTO, OneShotRespDTO
from model.user import UserDTO
from PIL import Image

app_config = config.get_config()
os_db = OneShotDB()


class ImageService:
    async def upload_image(
        self, user: UserDTO, oneshot: OneShotDTO, file: UploadFile
    ) -> str:
        file_extension = (
            file.filename[file.filename.rfind(".") + 1 :].lower()
            if "." in file.filename
            else None
        )

        if file_extension is None:
            raise ImgFileExtensionException()

        file_name = OneShotFileNameDTO(
            file_name=oneshot.get_file_name_no_ext(), file_extension=file_extension
        )  # for validation

        file_name = file_name.get_file_name()

        folder_path = os.path.join(app_config.WEBROOT_PATH, "img", user.username)
        path = os.path.join(folder_path, file_name)
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

        await self.__create_preview(folder_path, file_name)

        db_oneshot = DBOneShot(
            username=user.username,
            date=oneshot.date,
            time=oneshot.time,
            file_name=file_name,
            happiness=oneshot.happiness,
            text=oneshot.text,
        )
        await os_db.create_oneshot(db_oneshot)

        return file_name

    async def __create_preview(self, folder_path, file_name):
        # todo make this async. It is blocking.
        max_size = (450, 450)
        try:
            image = Image.open(os.path.join(folder_path, file_name))
            image.thumbnail(max_size)
            image.save(
                os.path.join(folder_path, f"preview.{file_name}"),
                optimize=True,
                quality=85,
            )
        except:
            raise UnprocessableImageException()

    async def download_image_by_date(
        self, user: UserDTO, date: DateDTO, is_preview=False
    ) -> FileResponse:
        oneshot = await os_db.get_oneshot(user.username, date)

        if oneshot is None:
            raise NoOneShotInDBFoundException()

        img_path = os.path.join(
            app_config.WEBROOT_PATH,
            "img",
            user.username,
            f"preview.{oneshot.file_name}" if is_preview else oneshot.file_name,
        )

        if os.path.exists(img_path) and os.path.isfile(img_path):
            return FileResponse(img_path)
        else:
            raise NoOneShotImgFoundException()

    async def download_image_by_file_name(
        self, user: UserDTO, file_name: OneShotFileNameDTO, is_preview=False
    ) -> FileResponse:
        img_path = os.path.join(
            app_config.WEBROOT_PATH,
            "img",
            user.username,
            f"preview.{file_name.get_file_name()}"
            if is_preview
            else file_name.get_file_name(),
        )

        if os.path.exists(img_path) and os.path.isfile(img_path):
            return FileResponse(img_path)
        else:
            raise NoOneShotImgFoundException()

    async def paginate_gallery(
        self, user: UserDTO, page: int, max_page_size: int
    ) -> list[OneShotRespDTO]:
        if max_page_size >= 1000 or max_page_size <= 0:
            raise InvalidPageSizeException

        oneshots = await os_db.get_gallery_page(user.username, page, max_page_size)
        return [OneShotRespDTO.from_db_oneshot(i) for i in oneshots]

    async def delete_image(self, user: UserDTO, date: DateDTO) -> str:
        await os_db.delete_image(user.username, date)
        return "ok"

    async def get_metadata(self, user: UserDTO, date: DateDTO) -> OneShotRespDTO:
        oneshot = await os_db.get_oneshot(user.username, date)

        if oneshot is None:
            raise NoOneShotInDBFoundException()

        return OneShotRespDTO.from_db_oneshot(oneshot)
