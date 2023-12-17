from datetime import datetime

from core import config
from core.exception import ImgFileExtensionException, ImgFileNameException
from model.happiness import HappinessDTO
from prisma.models import OneShot as DBOneShot
from pydantic import BaseModel, validator


class OneShotDTO(BaseModel):
    date: str  # YYYY-MM-YY format
    time: int  # Unix timestamp
    happiness: HappinessDTO | None = None
    text: str | None = None

    @validator("date")
    def validate_date_format(cls, v):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD). strftime again to add leading zeros.
            return datetime.strptime(v, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            from fastapi import HTTPException
            from starlette import status

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid date format. Expected YYYY-MM-DD.",
            )

    @validator("time")
    def validate_unix_timestamp(cls, v):
        if v < 0:
            from fastapi import HTTPException
            from starlette import status

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Timestamp must be a positive integer.",
            )
        return v

    def get_file_name_no_ext(self) -> str:
        dt_object = datetime.fromtimestamp(self.time)

        # Format the datetime object as YYYYMMDDHHMMSS
        file_naming_number = dt_object.strftime("%Y%m%d%H%M%S")

        return "OneShot_" + str(file_naming_number)


class OneShotRespDTO(OneShotDTO):
    """
    Output model for a OneShot.
    """

    file_name: str

    def from_db_oneshot(oneshot: DBOneShot):
        return OneShotRespDTO(
            date=oneshot.date,
            time=oneshot.time.timestamp(),
            happiness=oneshot.happiness,
            text=oneshot.text,
            file_name=oneshot.file_name,
        )


class OneShotFileNameDTO(BaseModel):
    file_name: str
    file_extension: str

    def get_file_name(self):
        return f"{self.file_name}.{self.file_extension}"

    @validator("file_extension")
    def validate_file_extension(cls, v):
        if v not in config.get_config().ONESHOT_ALLOWED_FILE_EXTENSIONS:
            raise ImgFileExtensionException()
        return v

    @validator("file_name")
    def validate_file_name(cls, v):
        import re

        if not re.match(r"^OneShot_\d{14}$", v):
            raise ImgFileNameException()
        return v
