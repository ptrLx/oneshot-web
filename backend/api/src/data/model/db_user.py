from model.user import User


class DBUser(User):
    hashed_password: str
