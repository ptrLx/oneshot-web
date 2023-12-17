from core import config
from prisma.models import User as DBUser

app_config = config.get_config()


class UserDB:
    async def get_user(self, username: str) -> DBUser:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.user.find_first(
            where={"username": username},
        )

    async def change_password(self, username: str, new_hashed_password: str):
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.user.update(
            where={"username": username},
            data={"hashed_password": new_hashed_password},
        )
