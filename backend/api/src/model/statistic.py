from model.oneshot import OneShotRespDTO
from pydantic import BaseModel


class HappinessPercentage(BaseModel):
    VERY_HAPPY: int
    HAPPY: int
    NEUTRAL: int
    SAD: int
    VERY_SAD: int
    NOT_SPECIFIED: int


class StatisticDTO(BaseModel):
    happiness_current_week: HappinessPercentage
    happiness_current_month: HappinessPercentage
    happiness_current_year: HappinessPercentage
