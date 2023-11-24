from core import config
from model.date import Date
from prisma.errors import UniqueViolationError
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

    async def get_oneshot(self, username: str, date: Date) -> DBOneShot:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.oneshot.find_first(
            where={"username": username, "date": date.date}
        )
