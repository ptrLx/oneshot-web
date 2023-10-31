from datetime import datetime

from pydantic import BaseModel, validator


class Date(BaseModel):
    date: str

    @validator("date")
    def validate_date_format(cls, value):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD)
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD format.")
        return value


class Month(BaseModel):
    month: str

    @validator("month")
    def validate_month_format(cls, value):
        try:
            # Check if the input string matches the month format (YYYY-MM)
            datetime.strptime(value, "%Y-%m")
        except ValueError:
            raise ValueError("Invalid month format. Use YYYY-MM format.")
        return value
