import logging
import os
import sys

logger = logging.getLogger(__name__)

import bcrypt
from admcore.config import commands, welcome_msg
from admcore.exception import (
    CLICoreException,
    NoDisabledUserException,
    NoOneShotCreatedException,
    NoUserCreatedException,
    NoUserEnabledUserException,
)
from admdata.oneshot_table import ADMOneShotDB, DBOneShot
from admdata.user_table import ADMUserDB, DBUser
from admservice.importer.handler import start_importer_cli
from core import config
from core.exception import HTTPException
from InquirerPy import inquirer
from model.date import DateDTO
from model.user import UserRoleDTO
from prisma.engine.errors import EngineConnectionError
from prisma.errors import ForeignKeyViolationError, UniqueViolationError

app_config = config.get_config()
user_db = ADMUserDB()
os_db = ADMOneShotDB()


class CLI:
    async def start(self) -> None:
        print(welcome_msg)

        while True:
            try:
                result = await inquirer.select(
                    message="What do you want do do?",
                    choices=commands.values(),
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
                elif result == commands["CMD_RESET_USER_PASSWORD"]:
                    await self.__handle_reset_user_password()
                elif result == commands["CMD_MODIFY"]:
                    await self.__handle_modify_oneshot_date()
                else:  # CMD_EXIT
                    print("\n👋 Bye bye.\n")
                    break

            except KeyboardInterrupt:
                print("\n❌ Aborted.\n")
                sys.exit(0)
            except EngineConnectionError:
                print("\n🔃 Couldn't connect to database.")
            except (CLICoreException, HTTPException) as e:
                print(f"\n❌ {e.detail}")

            print()

    async def __choose_user(
        self, only_enabled: bool = False, only_disabled: bool = False
    ) -> DBUser:
        assert not (only_disabled and only_enabled)

        if only_enabled:
            users = await user_db.get_enabled_users()
            if not len(users):
                raise NoUserEnabledUserException
        elif only_disabled:
            users = await user_db.get_disabled_users()
            if not len(users):
                raise NoDisabledUserException
        else:
            users = await user_db.get_users()
            if not len(users):
                raise NoUserCreatedException

        username = await inquirer.select(
            message="Choose an user:",
            choices=[user.username for user in users],
        ).execute_async()

        for user in users:
            if user.username == username:
                return user

    async def __choose_oneshot(self, username: str) -> DBOneShot:
        oneshots = await os_db.get_gallery_page(
            username=username, page=0, max_page_size=100
        )

        if not len(oneshots):
            raise NoOneShotCreatedException

        date = await inquirer.select(
            message="Choose an OneShot:",
            choices=[oneshot.date for oneshot in oneshots],
        ).execute_async()

        for oneshot in oneshots:
            if oneshot.date == date:
                return oneshot

    async def __handle_user_create(self) -> None:
        username = await inquirer.text(message="Username:").execute_async()

        user = await user_db.get_user(username)

        if user is not None:
            print("\n❌ User {username} already exists.")
            return

        password_1 = await inquirer.secret(message="Password:").execute_async()
        password_2 = await inquirer.secret(message="Retype password:").execute_async()

        if password_1 != password_2:
            print(f"\n❌ Passwords do not match.")
            return

        full_name = await inquirer.text(message="Full name:").execute_async()
        role = await inquirer.select(
            message="Select a role:", choices=[role.value for role in UserRoleDTO]
        ).execute_async()
        try:
            user = await user_db.create_user(
                username=username,
                role=role,
                disabled=False,
                full_name=full_name,
                hashed_password=bcrypt.hashpw(
                    password_1.encode(), bcrypt.gensalt()
                ).decode(),
            )
        except UniqueViolationError:
            print(f"\n❌ User {username} already exists.")
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

    async def __handle_user_delete(self) -> None:
        user = await self.__choose_user()

        confirmation = await inquirer.confirm(
            message=f"Do you really want to delete user {user.full_name} ({user.username})?",
        ).execute_async()

        if confirmation:
            # todo delete files?
            # todo delete oneshots from db?
            try:
                await user_db.delete_user(user.username)
                print("\n🗑  User deleted.")
            except ForeignKeyViolationError:
                print(
                    "\n❌ This user has existing OneShots in the database and cannot be deleted (a feature to delete all Oneshots first is currently not implemented)."
                )
        else:
            print("\n❌ Aborted.")

    async def __handle_import(self) -> None:
        user = await self.__choose_user()

        await start_importer_cli(user)

    async def __handle_export(self) -> None:
        user = await self.__choose_user()
        logger.error("Not implemented yet.")

    async def __handle_disable_user(self) -> None:
        user = await self.__choose_user(only_enabled=True)

        confirmation = await inquirer.confirm(
            message=f"Do you really want to disable user {user.full_name} ({user.username})?",
        ).execute_async()

        if confirmation:
            await user_db.disable_user(user.username)
            print("\n🙅 User disabled.")
        else:
            print("\n❌ Aborted.")

    async def __handle_enable_user(self) -> None:
        user = await self.__choose_user(only_disabled=True)

        if user is None:
            print("\n❌ User doesn't exist.")
            return

        confirmation = await inquirer.confirm(
            message=f"Do you really want to enable user {user.full_name} ({user.username})?",
        ).execute_async()

        if confirmation:
            await user_db.enable_user(user.username)
            print("\n💁 User enabled.")
        else:
            print("\n❌ Aborted.")

    async def __handle_list_users(self) -> None:
        users = await user_db.get_users()
        if len(users):
            print()
            [print(user) for user in users]
        else:
            print("No user exists. Try to create one.")

    async def __handle_reset_user_password(self) -> None:
        user = await self.__choose_user()

        if user is None:
            print("❌ User doesn't exist.")
            return

        password_1 = await inquirer.secret(message="New password:").execute_async()
        password_2 = await inquirer.secret(
            message="Retype new password:"
        ).execute_async()

        if password_1 != password_2:
            print(f"\n❌ Passwords do not match.")
            return

        confirmation = await inquirer.confirm(
            message=f"Do you really want to reset password of {user.full_name} ({user.username})?",
        ).execute_async()

        if confirmation:
            await user_db.change_password(
                user.username,
                bcrypt.hashpw(password_1.encode(), bcrypt.gensalt()).decode(),
            )
            print("\n↩️  Password changed.")
        else:
            print("\n❌ Aborted.")

    async def __handle_modify_oneshot_date(self) -> None:
        user = await self.__choose_user()

        oneshot = await self.__choose_oneshot(user.username)

        new_date = await inquirer.text("New date:").execute_async()

        # Validate date
        DateDTO(date=new_date)

        await os_db.update_date(oneshot, new_date)

        print("\n↩️  Updated.")
