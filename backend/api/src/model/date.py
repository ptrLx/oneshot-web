from datetime import datetime

from pydantic import BaseModel, validator


class Date(BaseModel):
    date: str

    @validator("date")
    def validate_date_format(cls, v):
        try:
            # Check if the input string matches the date format (YYYY-MM-DD)
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            from fastapi import HTTPException
            from starlette import status

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid date format. Expected YYYY-MM-DD.",
            )
        return v


# todo remove?
# class Month(BaseModel):
#     month: str

#     @validator("month")
#     def validate_month_format(cls, v):
#         try:
#             # Check if the input string matches the month format (YYYY-MM)
#             datetime.strptime(v, "%Y-%m")
#         except ValueError:
#             raise ValueError("Invalid month format. Expected YYYY-MM.")
#         return v
