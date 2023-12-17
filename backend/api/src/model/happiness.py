from enum import Enum


class HappinessDTO(str, Enum):
    VERY_HAPPY = "VERY_HAPPY"
    HAPPY = "HAPPY"
    NEUTRAL = "NEUTRAL"
    SAD = "SAD"
    VERY_SAD = "VERY_SAD"
