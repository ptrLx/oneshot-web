from starlette import status
from fastapi import HTTPException

class NoProfileImg(HTTPException):
    def __init__(self):
        #// self.custom_data = custom_data
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="No profile image found.")
