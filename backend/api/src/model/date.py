from datetime import datetime

from core.exception import InvalidDateFormatException, InvalidMonthFormatException
from model.oneshot import OneShotRespDTO
from pydantic import BaseModel, validator


class DateDTO(BaseModel):
    date: str

    @validator("date")
    def validate_date_format(cls, v):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD). strftime again to add leading zeros.
            return datetime.strptime(v, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            raise InvalidDateFormatException


class MonthDTO(BaseModel):
    month: str

    @validator("month")
    def validate_month_format(cls, v):
        try:
            # Check if the input string matches the month format (YYYY-MM). strftime again to add leading zeros.
            return datetime.strptime(v, "%Y-%m").strftime("%Y-%m")
        except ValueError:
            raise InvalidMonthFormatException


class CalendarEntryRespDTO(BaseModel):
    date: str
    oneshot: OneShotRespDTO | None = None
