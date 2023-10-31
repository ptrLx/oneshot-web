import json
import logging
import os
import sys

from core.setup import (
    bootstrap_db,
    bootstrap_filesystem,
    db_is_initialized,
    filesystem_is_initialized,
)


class AppConfig:
    def __init__(self) -> None:
        self.__config_logging_level()

        self.WEBROOT_PATH = os.getenv("WEBROOT_PATH", "/srv/oneshot/")

        if not filesystem_is_initialized(self.WEBROOT_PATH):
            bootstrap_filesystem(self.WEBROOT_PATH)

        if not db_is_initialized():
            bootstrap_db()

        self.SECRET_KEY = self.__read_config()
        self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES", 259200
        )  # defaults to 180 days
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")

    def __config_logging_level(self):
        level = os.getenv("LOGGING_LEVEL", "INFO").upper()

        if level == "DEBUG":
            self.LOGGING_LEVEL = logging.DEBUG
        elif level == "INFO":
            self.LOGGING_LEVEL = logging.INFO
        elif level == "WARNING":
            self.LOGGING_LEVEL = logging.WARNING
        elif level == "ERROR":
            self.LOGGING_LEVEL = logging.ERROR
        elif level == "CRITICAL":
            self.LOGGING_LEVEL = logging.CRITICAL
        else:
            self.LOGGING_LEVEL = logging.INFO

        logging.basicConfig(
            level=self.LOGGING_LEVEL, format="%(asctime)s [%(levelname)s] %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def __read_config(self):
        with open(f"{self.WEBROOT_PATH}/conf.json", "r") as file:
            data = json.load(file)

        try:
            SECRET_KEY = data["SECRET_KEY"]
        except KeyError:
            self.logger.error(f"No secret key found in {self.WEBROOT_PATH}/conf.json.")
            sys.exit(1)

        return SECRET_KEY


#todo use same config object in all files
global app_config
app_config = AppConfig()
