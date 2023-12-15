from model.oneshot import OneShotRespDTO
from pydantic import BaseModel


class FlashbackDTO(BaseModel):
    random_happy: OneShotRespDTO | None = None
    last_very_happy_day: OneShotRespDTO | None = None
    same_day_last_month: OneShotRespDTO | None = None
    same_date_last_years: list[OneShotRespDTO]
