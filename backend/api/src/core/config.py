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

        self.WEBROOT_PATH = os.getenv("WEBROOT_PATH", "/srv/oneshot")

        if not filesystem_is_initialized(self.WEBROOT_PATH):
            bootstrap_filesystem(self.WEBROOT_PATH)

        if not db_is_initialized():
            bootstrap_db()

        self.SECRET_KEY = self.__read_config()
        self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES", 259200
        )  # defaults to 180 days
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")
        self.ONESHOT_ALLOWED_FILE_EXTENSIONS = (
            os.getenv("ONESHOT_ALLOWED_FILE_EXTENSIONS", "jpg, png, jpeg")
            .lower()
            .replace(" ", "")
            .split(",")
        )

        self.STAGE = os.getenv("STAGE", "prod")

        # for CORS:
        # Defaults to the default local frontend port.
        # In production both api and frontend are behind the same nginx and thus behind the same host url.
        # Use "*" to disable CORS.
        self.HOST_URL = os.getenv("HOST_URL")
        if self.HOST_URL is None:
            if self.STAGE == "dev":
                self.HOST_URL = "http://localhost:8100"  # Needed for CORS. The actual HOST_URL would be http://localhost:8200
            else:
                self.logger.error(f"HOST_URL environment variable is not set.")
                sys.exit(1)

        self.MAX_FILE_UPLOAD_CHUNK_SIZE_B = os.getenv(
            "MAX_FILE_UPLOAD_CHUNK_SIZE_B", 1024 * 1024
        )  # Default is 1MB

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
        conf_path = os.path.join(self.WEBROOT_PATH, "conf.json")
        with open(conf_path, "r") as file:
            data = json.load(file)

        try:
            SECRET_KEY = data["SECRET_KEY"]
        except KeyError:
            self.logger.error(f"No secret key found in {conf_path}.")
            sys.exit(1)

        return SECRET_KEY


def get_config() -> AppConfig:
    if not hasattr(get_config, "app_config"):
        setattr(get_config, "app_config", AppConfig())
    return get_config.app_config
