from core import config
from core.exception import NoOneShotInDBFoundException
from model.date import DateDTO
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
