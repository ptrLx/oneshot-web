from model.user import UserInDB

__fake_users_db = {
    "john": {
        "username": "john",
        "role": "admin",
        "disabled": False,
        "full_name": "John Doe",
        "hashed_password": "$2b$12$oXRsA3Kf1s3y8yx7dYGpl.hcAk.NFBYDuwyerL3pFO978vfuhW7d2",  # password
    }
}


def get_user(username: str):
    if username in __fake_users_db:
        user_dict = __fake_users_db[username]
        return UserInDB(**user_dict)
