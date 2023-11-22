from typing import List

from core import config
from model.user import UserRole
from prisma.models import User as DBUser

app_config = config.get_config()


class UserDB:
    async def create_user(
        self,
        username: str,
        hashed_password: str,
        role: UserRole = "USER",
        disabled: bool = False,
        full_name: str = None,
    ) -> DBUser:
        prisma = await app_config.get_prisma_conn()
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
        await prisma.user.delete(
            where={"username": username},
        )
        # todo delete other table entries?

    async def get_user(self, username: str) -> DBUser:
        prisma = await app_config.get_prisma_conn()
        return await prisma.user.find_first(
            where={"username": username},
        )

    async def get_users(self) -> List[DBUser]:
        prisma = await app_config.get_prisma_conn()
        return await prisma.user.find_many(take=9999)

    async def change_password(self, username: str, new_hashed_password: str):
        prisma = await app_config.get_prisma_conn()
        return await prisma.user.update(
            where={"username": username},
            data={"hashed_password": new_hashed_password},
        )
