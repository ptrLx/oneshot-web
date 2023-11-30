from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from model.date import Date
from model.user import User
from service.image import ImageService
from service.validate import get_current_active_user

router = APIRouter()

image_service = ImageService()


@router.get("/")
async def download_preview(
    current_user: Annotated[User, Depends(get_current_active_user)],
    date: str,
) -> FileResponse:
    return await image_service.download_image_by_date(
        current_user, Date(date=date), is_preview=True
    )
