from enum import Enum


class Happiness(str, Enum):
    NOT_SPECIFIED = "NOT_SPECIFIED"
    VERY_HAPPY = "VERY_HAPPY"
    HAPPY = "HAPPY"
    NEUTRAL = "NEUTRAL"
    SAD = "SAD"
    VERY_SAD = "VERY_SAD"


# todo remove?
# # Either a Happiness or NO_ENTRY
# class HappinessState(str, Enum):
#     NOT_SPECIFIED = "NOT_SPECIFIED"
#     VERY_HAPPY = "VERY_HAPPY"
#     HAPPY = "HAPPY"
#     NEUTRAL = "NEUTRAL"
#     SAD = "SAD"
#     VERY_SAD = "VERY_SAD"
#     NO_ENTRY = "NO_ENTRY"
