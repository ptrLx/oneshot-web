from fastapi import Depends, APIRouter
from fastapi.responses import FileResponse
from typing import Annotated
from model.user import User
from typing import Annotated

from service.user import UserService

from service.validate import get_current_active_user

router = APIRouter()

user_service = UserService()


@router.get("/me", response_model=User)
async def get_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return user_service.get_user_info(current_user)


@router.get("/profileimg")
async def get_user_profile_img(
    _current_user: Annotated[User, Depends(get_current_active_user)]
):
    return FileResponse("../../_sample/test-profile-img.png")


@router.post("chpw")
async def change_user_password(
    old_password,
    new_password,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return user_service.change_password(old_password, new_password, current_user)
