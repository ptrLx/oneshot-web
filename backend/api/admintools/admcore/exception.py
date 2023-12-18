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
