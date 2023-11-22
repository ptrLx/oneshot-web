import asyncio
import logging
import sys

logger = logging.getLogger(__name__)

import bcrypt
from admcore.config import (
    CMD_CREATE_USER,
    CMD_DELETE_USER,
    CMD_EXPORT,
    CMD_IMPORT,
    welcome_msg,
)
from data.user_db import UserDB
from InquirerPy import inquirer
from model.user import UserRole

user_db = UserDB()


class CLI:
    def __init__(self) -> None:
        self.commands = [CMD_CREATE_USER, CMD_DELETE_USER, CMD_IMPORT, CMD_EXPORT]

    def start(self) -> None:
        print(welcome_msg)

        try:
            result = inquirer.select(
                message="What do you want do do?",
                choices=self.commands,
            ).execute()

            if result == CMD_CREATE_USER:
                self.__handle_user_create()
            elif result == CMD_DELETE_USER:
                self.__handle_user_delete()
            elif result == CMD_IMPORT:
                self.__handle_import()
            elif result == CMD_EXPORT:
                self.__handle_export()

        except KeyboardInterrupt:
            print("❌ Aborted.")
            sys.exit(0)

    def __handle_user_create(self):
        username = inquirer.text(message="username:").execute()
        password = inquirer.secret(message="password:").execute()
        role = inquirer.select(
            message="Select a role:", choices=[role.value for role in UserRole]
        ).execute()
        full_name = inquirer.text(message="Full name").execute()
        # try:
        user = asyncio.run(
            user_db.create_user(
                username=username,
                role=role,
                disabled=False,
                full_name=full_name,
                hashed_password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
            )
        )
        print("\n🪄 User created.")
        # except :
        #     # todo handle username exists, no connection to database

    def __handle_user_delete(self):
        logger.error("Not implemented yet.")

    def __handle_import(self):
        logger.error("Not implemented yet.")

    def __handle_export(self):
        logger.error("Not implemented yet.")
