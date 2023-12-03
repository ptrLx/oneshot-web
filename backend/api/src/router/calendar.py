from typing import Annotated

from fastapi import APIRouter, Depends
from model.date import CalendarEntryRespDTO, MonthDTO
from model.user import UserDTO
from service.calendar import CalendarService
from service.validate import get_current_active_user

router = APIRouter()

calendar_service = CalendarService()


@router.get("/")
async def get_calendar(
    current_user: Annotated[UserDTO, Depends(get_current_active_user)], month: str
) -> list[CalendarEntryRespDTO]:
    return await calendar_service.get_calendar(current_user, MonthDTO(month=month))
