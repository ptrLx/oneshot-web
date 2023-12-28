from typing import List

from core import config
from data.user_table import UserDB
from model.user import UserRoleDTO
from prisma.models import User as DBUser

app_config = config.get_config()


class ADMUserDB(UserDB):
    async def create_user(
        self,
        username: str,
        hashed_password: str,
        role: UserRoleDTO = "USER",
        disabled: bool = False,
        full_name: str = None,
    ) -> DBUser:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.user.create(
            data={
                "username": username,
                "hashed_password": hashed_password,
                "role": role,
                "disabled": disabled,
                "full_name": full_name,
            }
        )

    async def delete_user(self, username: str) -> None:
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        await prisma.user.delete(
            where={"username": username},
        )

    async def get_users(self) -> List[DBUser]:
        prisma = await app_config.get_prisma_conn()

        return await prisma.user.find_many(take=9999)

    async def get_enabled_users(self) -> List[DBUser]:
        prisma = await app_config.get_prisma_conn()

        return await prisma.user.find_many(take=9999, where={"disabled": False})

    async def get_disabled_users(self) -> List[DBUser]:
        prisma = await app_config.get_prisma_conn()

        return await prisma.user.find_many(take=9999, where={"disabled": True})

    async def disable_user(self, username: str):
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.user.update(
            where={"username": username},
            data={"disabled": True},
        )

    async def enable_user(self, username: str):
        prisma = await app_config.get_prisma_conn()

        username = username.lower()

        return await prisma.user.update(
            where={"username": username},
            data={"disabled": False},
        )
