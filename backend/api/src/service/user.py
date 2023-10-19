from model.user import User


class UserService:
    def get_user_info(self, user: User):
        return user

    def change_password(self, old_password: str, new_password: str, user: User):
        # todo verify old pw, create new hash, update db
        return "ok"
