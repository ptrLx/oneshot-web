from typing import Annotated

import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile
from model.user import User
from service.validate import get_current_active_user

router = APIRouter()


MAX_FILE_SIZE_B = 1024 * 1024  # 1MB


@router.post("/upload")
async def upload_image(
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile = File(...),
):
    path = f"../../_local-data/image/{current_user.username}/{file.filename}"
    try:
        async with aiofiles.open(path, "wb") as f:
            while contents := await file.read(MAX_FILE_SIZE_B):
                await f.write(contents)

    except Exception:
        return {"message": "There was an error uploading the file"}  # todo
    finally:
        await file.close()

    return "ok"
