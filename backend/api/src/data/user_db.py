from core import config
from model.user import UserInDB

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

    async def get_user(self, username: str):
        prisma = await app_config.get_prisma()
        if username in self.__fake_users_db:
            user_dict = self.__fake_users_db[username]
            return UserInDB(**user_dict)
