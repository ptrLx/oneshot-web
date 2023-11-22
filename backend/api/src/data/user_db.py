from core import config
from model.user import UserRole
from prisma.models import User as DBUser

app_config = config.get_config()


class UserDB:
    def __init__(self) -> None:
        self.__fake_users_db = {
            "john": {
                "username": "john",
                "role": "ADMIN",
                "disabled": False,
                "full_name": "John Doe",
                "hashed_password": "$2b$12$oXRsA3Kf1s3y8yx7dYGpl.hcAk.NFBYDuwyerL3pFO978vfuhW7d2",  # password
            }
        }

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
                "hashed_password": str(hashed_password),
                "role": role,
                "disabled": disabled,
                "full_name": full_name,
            }
        )

    async def user_exists(self, username: str) -> bool:
        prisma = await app_config.get_prisma_conn()
        return username in self.__fake_users_db

    async def get_user(self, username: str) -> DBUser:
        prisma = await app_config.get_prisma_conn()
        if await self.user_exists(username):
            user_dict = self.__fake_users_db[username]
            return DBUser(**user_dict)

        return None
