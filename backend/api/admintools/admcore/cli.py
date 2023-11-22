import logging
import sys

logger = logging.getLogger(__name__)

import bcrypt
from admcore.config import commands, welcome_msg
from data.user_db import UserDB
from InquirerPy import inquirer
from model.user import UserRole
from prisma.errors import UniqueViolationError

user_db = UserDB()


class CLI:
    def __init__(self) -> None:
        self.commands = commands

    async def start(self) -> None:
        print(welcome_msg)

        try:
            while True:
                result = await inquirer.select(
                    message="What do you want do do?",
                    choices=self.commands.values(),
                ).execute_async()

                if result == commands["CMD_CREATE_USER"]:
                    await self.__handle_user_create()
                elif result == commands["CMD_DELETE_USER"]:
                    await self.__handle_user_delete()
                elif result == commands["CMD_IMPORT"]:
                    await self.__handle_import()
                elif result == commands["CMD_EXPORT"]:
                    await self.__handle_export()
                elif result == commands["CMD_LIST_USERS"]:
                    await self.__list_users()
                else:  # CMD_EXIT
                    print("👋 Bye bye.")
                    break

                print()

        except KeyboardInterrupt:
            print("❌ Aborted.")
            sys.exit(0)

    async def __handle_user_create(self):
        username = await inquirer.text(message="username:").execute_async()
        password = await inquirer.secret(message="password:").execute_async()
        full_name = await inquirer.text(message="Full name").execute_async()
        role = await inquirer.select(
            message="Select a role:", choices=[role.value for role in UserRole]
        ).execute_async()
        try:
            user = await user_db.create_user(
                username=username,
                role=role,
                disabled=False,
                full_name=full_name,
                hashed_password=bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt()
                ).decode(),
            )

            print("\n🪄  User created.")
        except UniqueViolationError:
            logging.error(f"User {username} already exists.")

        # todo handle no connection to database

    async def __handle_user_delete(self):
        username = await inquirer.text(message="username:").execute_async()

        # todo get user name and check if exists
        full_name = "John"

        confirmation = await inquirer.confirm(
            message=f"Do you really want to delete user {full_name} ({username})?",
        ).execute_async()

        if confirmation:
            await user_db.delete_user(username)
            # todo delete files?
            # todo delete all db entries?
            print("\n🗑  User deleted.")
        else:
            print("❌ Aborted.")

    async def __handle_import(self):
        logger.error("Not implemented yet.")

    async def __handle_export(self):
        logger.error("Not implemented yet.")

    async def __list_users(self):
        users = await user_db.get_users()
        if len(users):
            [print(user) for user in users]
        else:
            print("No user exists. Try to create one.")
