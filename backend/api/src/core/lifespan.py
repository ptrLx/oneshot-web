import logging
from contextlib import asynccontextmanager

from core import config
from fastapi import FastAPI
from prisma import Prisma

app_config = config.get_config()
logger = logging.getLogger(__name__)


async def __graceful_exit() -> None:
    prisma = app_config.get_prisma_no_conn()
    if prisma.is_connected():
        await prisma.disconnect()
        logger.info("Database connection closed.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # * This will run before startup

    # Nothing to do here

    yield

    # * This will run before termination

    await __graceful_exit()
