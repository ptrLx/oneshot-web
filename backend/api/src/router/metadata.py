from typing import Annotated

from fastapi import APIRouter, Depends
from model.date import DateDTO
from model.oneshot import OneShotRespDTO
from model.user import UserDTO
from service.image import ImageService
from service.validate import get_current_active_user

image_service = ImageService()

router = APIRouter()


@router.get("/")
async def get_metadata(
    current_user: Annotated[UserDTO, Depends(get_current_active_user)],
    date: str | None = None,
) -> OneShotRespDTO:
    return await image_service.get_metadata(current_user, DateDTO(date=date))
