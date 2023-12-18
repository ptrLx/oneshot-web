import logging

from admdata.user_table import DBUser
from InquirerPy import inquirer

logger = logging.getLogger(__name__)


class MetadataImporter:
    def __init__(self, user: DBUser) -> None:
        self.user = user

    async def start(self):
        location = await inquirer.text(
            "Specify a folder where the images that should be imported are stored:"
        ).execute_async()

        logger.error("Not implemented yet.")
