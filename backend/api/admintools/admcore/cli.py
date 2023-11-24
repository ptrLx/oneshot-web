import logging
import os
import sys

logger = logging.getLogger(__name__)

import bcrypt
from admcore.config import commands, welcome_msg
from core import config
from data.user_table import UserDB
from InquirerPy import inquirer
from model.user import UserRole
from prisma.errors import UniqueViolationError

app_config = config.get_config()
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
                    await self.__handle_list_users()
                elif result == commands["CMD_DISABLE_USER"]:
                    await self.__handle_disable_user()
                elif result == commands["CMD_ENABLE_USER"]:
                    await self.__handle_enable_user()
                else:  # CMD_EXIT
                    print("👋 Bye bye.")
                    break

                print()

        except KeyboardInterrupt:
            print("❌ Aborted.")
            sys.exit(0)

    async def __handle_user_create(self) -> None:
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
        except UniqueViolationError:
            print(f"❌ User {username} already exists.")
            return

        try:
            os.makedirs(
                os.path.join(app_config.WEBROOT_PATH, "img", username),
                exist_ok=False,
            )
        except FileExistsError:
            logger.warn(
                f"User image directory for {username} already exists. Be careful!"
            )

        print("\n🪄  User created.")

        # todo handle no connection to database

    async def __handle_user_delete(self) -> None:
        username = await inquirer.text(message="username:").execute_async()

        user = await user_db.get_user(username)

        if user is None:
            print("❌ User doesn't exist.")
            return

        confirmation = await inquirer.confirm(
            message=f"Do you really want to delete user {user.full_name} ({username})?",
        ).execute_async()

        if confirmation:
            await user_db.delete_user(username)
            # todo delete files?
            # todo delete all db entries?
            print("\n🗑  User deleted.")
        else:
            print("❌ Aborted.")

    async def __handle_import(self) -> None:
        logger.error("Not implemented yet.")

    async def __handle_export(self) -> None:
        logger.error("Not implemented yet.")

    async def __handle_disable_user(self) -> None:
        username = await inquirer.text(message="username:").execute_async()

        user = await user_db.get_user(username)

        if user is None:
            print("❌ User doesn't exist.")
            return

        confirmation = await inquirer.confirm(
            message=f"Do you really want to disable user {user.full_name} ({username})?",
        ).execute_async()

        if confirmation:
            await user_db.disable_user(username)
            print("\n🙅 User disabled.")
        else:
            print("❌ Aborted.")

    async def __handle_enable_user(self) -> None:
        username = await inquirer.text(message="username:").execute_async()

        user = await user_db.get_user(username)

        if user is None:
            print("❌ User doesn't exist.")
            return

        confirmation = await inquirer.confirm(
            message=f"Do you really want to enable user {user.full_name} ({username})?",
        ).execute_async()

        if confirmation:
            await user_db.enable_user(username)
            print("\n💁 User enabled.")
        else:
            print("❌ Aborted.")

    async def __handle_list_users(self) -> None:
        users = await user_db.get_users()
        if len(users):
            [print(user) for user in users]
        else:
            print("No user exists. Try to create one.")
