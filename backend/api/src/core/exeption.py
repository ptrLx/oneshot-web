from fastapi import HTTPException
from starlette import status


class NoProfileImg(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="No profile image found."
        )


class ImgUploadException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurred during the file upload.",
        )


class ImgFileExtensionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File extension not allowed.",
        )
