from core import config
from data.oneshot_table import DBOneShot, OneShotDB

app_config = config.get_config()


class ADMOneShotDB(OneShotDB):
    async def update_date(self, oneshot: DBOneShot, new_date: str) -> None:
        prisma = await app_config.get_prisma_conn()

        await prisma.oneshot.update(
            where={
                "username_date": {
                    "username": oneshot.username,
                    "date": oneshot.date,
                }
            },
            data={
                "date": new_date,
            },
        )
