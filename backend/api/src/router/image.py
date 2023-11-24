import os
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from model.date import Date
from model.oneshot import OneShot, OneShotFileName
from model.user import User
from service.image import ImageService
from service.validate import get_current_active_user
from starlette import status

router = APIRouter()

image_service = ImageService()


@router.post("/upload")
async def upload_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    oneshot: OneShot = Depends(),
    file: UploadFile = File(...),
) -> str:
    return await image_service.store_image(current_user, oneshot, file)


@router.get("/download")
async def download_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file_name: str | None = None,
    date: str | None = None,
) -> FileResponse:
    if date is None:
        if file_name is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Either a date or a file name is required.",
            )
        else:
            name, extension = os.path.splitext(file_name)
            # Remove the leading dot from the extension
            extension = extension[1:]

            file_name = OneShotFileName(file_name=name, file_extension=extension)

            return await image_service.download_image_by_file_name(
                current_user, file_name
            )
    elif file_name is None:
        return await image_service.download_image_by_date(current_user, Date(date=date))
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either a date or a file name is required but both where provided.",
        )


@router.post("/delete")
async def delete_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    date: str | None = None,
) -> str:
    pass  # todo
