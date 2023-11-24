from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from model.user import User
from service.validate import get_current_active_user

router = APIRouter()


@router.get("/")
async def download_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    date: str | None = None,
) -> FileResponse:
    pass  # todo
