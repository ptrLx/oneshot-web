from typing import Annotated

from fastapi import APIRouter, Depends
from model.statistic import StatisticDTO
from model.user import UserDTO
from service.image import ImageService
from service.validate import get_current_active_user

image_service = ImageService()

router = APIRouter()


@router.get("/")
async def get_statistics(
    current_user: Annotated[UserDTO, Depends(get_current_active_user)],
) -> StatisticDTO:
    return await image_service.get_statistics(current_user)
