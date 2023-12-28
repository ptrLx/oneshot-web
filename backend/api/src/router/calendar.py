from typing import Annotated

from fastapi import APIRouter, Depends
from model.date import CalendarEntryRespDTO, MonthDTO
from model.user import UserDTO
from service.image import ImageService
from service.validate import get_current_active_user

router = APIRouter()

image_service = ImageService()


@router.get("/")
async def get_calendar(
    current_user: Annotated[UserDTO, Depends(get_current_active_user)], month: str
) -> list[CalendarEntryRespDTO]:
    return await image_service.get_calendar(current_user, MonthDTO(month=month))
