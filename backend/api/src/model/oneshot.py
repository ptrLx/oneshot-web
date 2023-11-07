from datetime import datetime

from model.happiness import Happiness
from pydantic import BaseModel, validator


class OneShot(BaseModel):
    date: str  # YYYY-MM-YY format
    time: int  # Unix timestamp
    happiness: Happiness | None = None
    text: str | None = None

    @validator("date")
    def validate_date_format(cls, value):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD)
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-YY.")
        return value

    @validator("time")
    def validate_unix_timestamp(cls, value):
        if value < 0:
            raise ValueError("Unix timestamp must be a non-negative integer.")
        return value

    def get_file_name(self):
        dt_object = datetime.utcfromtimestamp(self.time)

        # Format the datetime object as YYYYMMDDHHMMSS
        file_naming_number = dt_object.strftime("%Y%m%d%H%M%S")

        return "OneShot_" + file_naming_number
