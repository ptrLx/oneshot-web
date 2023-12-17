from typing import Annotated

from fastapi import APIRouter, Depends
from model.flashback import FlashbackDTO
from model.user import UserDTO
from service.image import ImageService
from service.validate import get_current_active_user

image_service = ImageService()

router = APIRouter()


@router.get("/")
async def get_flashbacks(
    current_user: Annotated[UserDTO, Depends(get_current_active_user)],
) -> FlashbackDTO:
    return await image_service.get_flashbacks(current_user)
