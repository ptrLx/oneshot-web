import logging

from admcore.exception import CLICoreException
from admdata.user_table import DBUser
from admservice.importer.metadata.metadata_importer import MetadataImporter
from InquirerPy import inquirer

logger = logging.getLogger(__name__)


async def start_importer_cli(user: DBUser) -> None:
    sources = {
        "ANDROIDJSON": "Export JSON from the Android App",
        "OSWEBJSON": "Export JSON from os-web",
        "IMAGES": "Image files",
    }

    result = await inquirer.select(
        message="From which source do you want to import?",
        choices=sources.values(),
    ).execute_async()

    if result == sources["ANDROIDJSON"]:
        logger.error("Not implemented yet.")
    elif result == sources["OSWEBJSON"]:
        logger.error("Not implemented yet.")
    elif result == sources["IMAGES"]:
        importer = MetadataImporter(user)
        await importer.start()

    else:
        raise CLICoreException
