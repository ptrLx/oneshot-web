class CLICoreException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "CLI core Exception."


class UserNotExistsException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "User does not exist."


class NoUserCreatedException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "No user was found."


class NoDisabledUserException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "No disabled user was found."


class NoUserEnabledUserException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "No enabled user was found."


class NoOneShotCreatedException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "No oneshot was found for the selected user."


class DateExistsInDBException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "A OneShot for this date already exists."


class UserExistsInDBException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "A user with this username already exists."


class PasswordsNotMatchException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "Passwords do not match."


class AbortedException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "Aborted."


class UserHasOneShotsException(CLICoreException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.detail = "This user has existing OneShots in the database and cannot be deleted (a feature to delete all Oneshots first is currently not implemented)."
