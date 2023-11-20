from core import config
from data.model.db_user import DBUser

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

    async def user_exists(self, username: str) -> bool:
        prisma = await app_config.get_prisma_conn()
        return username in self.__fake_users_db

    async def get_user(self, username: str) -> DBUser:
        prisma = await app_config.get_prisma_conn()
        if await self.user_exists(username):
            user_dict = self.__fake_users_db[username]
            return DBUser(**user_dict)
