from core import config
from core.exception import NoOneShotInDBFoundException
from model.date import DateDTO, MonthDTO
from model.statistic import HappinessPercentage
from prisma.enums import Happiness
from prisma.models import OneShot as DBOneShot

app_config = config.get_config()


class OneShotDB:
    async def create_oneshot(self, oneshot: DBOneShot) -> None:
        prisma = await app_config.get_prisma_conn()

        await prisma.oneshot.upsert(
            where={
                "username_date": {
                    "username": oneshot.username,
                    "date": oneshot.date,
                }
            },
            data={
                "create": {
                    "username": oneshot.username,
                    "date": oneshot.date,
                    "file_name": oneshot.file_name,
                    "time": oneshot.time,
                    "happiness": oneshot.happiness,
                    "text": oneshot.text,
                },
                "update": {
                    "file_name": oneshot.file_name,
                    "time": oneshot.time,
                    "happiness": oneshot.happiness,
                    "text": oneshot.text,
                },
            },
        )

    async def get_oneshot(self, username: str, date: DateDTO) -> DBOneShot:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_first(
            where={"username": username, "date": date.date}
        )

    async def get_gallery_page(
        self, username: str, page: int, max_page_size: int
    ) -> list[DBOneShot]:
        """
        returns the next max_page_size OneShots and the start_date for the next page.
        """

        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_many(
            take=max_page_size,
            skip=max_page_size * page,
            order={"date": "desc"},
            where={"username": username},
        )

    async def get_last_ten_happy(self, username) -> list[DBOneShot]:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_many(
            take=10,
            order={"date": "desc"},
            where={
                "AND": [
                    {"username": username},
                    {
                        "OR": [
                            {"happiness": Happiness.HAPPY},
                            {"happiness": Happiness.VERY_HAPPY},
                        ]
                    },
                ]
            },
        )

    async def get_last_very_happy(self, username) -> DBOneShot:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_first(
            order={"date": "desc"},
            where={
                "AND": [{"username": username}, {"happiness": Happiness.VERY_HAPPY}]
            },
        )

    async def get_same_day_last_years(
        self, username, month_day: str
    ) -> list[DBOneShot]:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_many(
            order={"date": "desc"},
            where={"AND": [{"username": username}, {"date": {"endswith": month_day}}]},
        )

    async def get_calendar_month(
        self, username: str, month: MonthDTO
    ) -> list[DBOneShot]:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_many(
            order={"date": "asc"},
            where={
                "username": username,
                "date": {"startswith": month.month},
            },
        )

    async def delete_image(self, username: str, date: DateDTO) -> None:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        deleted_oneshot = await prisma.oneshot.delete(
            where={
                "username_date": {
                    "username": username,
                    "date": date.date,
                }
            },
        )

        if deleted_oneshot is None:
            raise NoOneShotInDBFoundException

    async def get_happiness_statistic(
        self, username: str, days: list[str] = None, month: str = None, year: str = None
    ) -> HappinessPercentage:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        if days is not None and month is None and year is None:
            date_criteria = {"in": days}
        elif days is None and month is not None and year is None:
            date_criteria = {"startswith": month}
        elif days is None and month is None and year is not None:
            date_criteria = {"startswith": year}
        else:
            raise ValueError

        happinesses = [
            user.happiness
            for user in await prisma.oneshot.find_many(
                where={"AND": [{"username": username}, {"date": date_criteria}]}
            )
        ]  # todo select happiness in query

        happiness_count = {
            "VERY_HAPPY": 0,
            "HAPPY": 0,
            "NEUTRAL": 0,
            "SAD": 0,
            "VERY_SAD": 0,
            "NOT_SPECIFIED": 0,
        }
        total_count = len(happinesses)
        if total_count:
            for i in happinesses:
                happiness_count[i] += 1
            happiness_percentage = {
                category: int(count * 100 / total_count)
                for category, count in happiness_count.items()
            }
        else:
            happiness_percentage = happiness_count

        return HappinessPercentage.model_validate(happiness_percentage)
