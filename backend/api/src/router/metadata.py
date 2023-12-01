from typing import Annotated

from fastapi import APIRouter, Depends
from model.oneshot import OneShotOut
from model.user import User
from service.validate import get_current_active_user

router = APIRouter()


# todo
# @router.get("/")
# async def get_metadata(
#     current_user: Annotated[User, Depends(get_current_active_user)],
#     date: str | None = None,
# ) -> OneShotOut:
#     pass
