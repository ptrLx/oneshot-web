from datetime import datetime

from core import config
from core.exception import ImgFileExtensionException, ImgFileNameException
from model.happiness import Happiness
from pydantic import BaseModel, validator


class OneShot(BaseModel):
    date: str  # YYYY-MM-YY format
    time: int  # Unix timestamp
    happiness: Happiness | None = None
    text: str | None = None

    @validator("date")
    def validate_date_format(cls, v):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD)
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-YY.")
        return v

    @validator("time")
    def validate_unix_timestamp(cls, v):
        if v < 0:
            raise ValueError("Unix timestamp must be a non-negative integer.")
        return v

    def get_file_name_no_ext(self) -> str:
        dt_object = datetime.fromtimestamp(self.time)

        # Format the datetime object as YYYYMMDDHHMMSS
        file_naming_number = dt_object.strftime("%Y%m%d%H%M%S")

        return "OneShot_" + str(file_naming_number)


class OneShotFileName(BaseModel):
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
