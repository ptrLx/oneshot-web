import os
import json
import logging
import secrets

logger = logging.getLogger(__name__)


def filesystem_is_initialized(webroot_path: str) -> bool:
    return os.path.exists(webroot_path) and os.path.isdir(webroot_path)


def bootstrap_filesystem(webroot_path: str) -> None:
    """
    Folder structure

    webroot_path/
    |-conf.json
    |-img/
      |-<user>/
        |-<OneShot_XXXXXXXXXXXXXX.jpg>
    """

    logger.info(f"Bootstrapping folder {webroot_path}")

    os.makedirs(f"{webroot_path}/img", exist_ok=True)

    logger.info(f"Generating secret key")

    SECRET_KEY = secrets.token_hex(32).upper()

    config_data = {"SECRET_KEY": SECRET_KEY}

    logger.info(f"Writing config file")

    with open(f"{webroot_path}/conf.json", "w") as f:
        json.dump(config_data, f, indent=4)


def db_is_initialized() -> bool:  # todo
    return True


def bootstrap_db() -> None:  # todo
    logger.info(f"Bootstrapping database")
