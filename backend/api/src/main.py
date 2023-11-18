import logging

from core import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.image import router as image_router
from router.login import router as login_router
from router.user import router as user_router

app_config = config.get_config()
logger = logging.getLogger(__name__)


app = FastAPI(
    docs_url=None
    if app_config.STAGE == "prod"
    else "/docs",  # Disable docs (Swagger UI) in production
    redoc_url=None
    if app_config.STAGE == "prod"
    else "/redoc",  # Disable redoc in production
)


origins = [app_config.HOST_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_status() -> str:
    return "ok"


app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(login_router, prefix="/login", tags=["Login"])
app.include_router(image_router, prefix="/image", tags=["Image"])

logger.info(f"Running in stage {app_config.STAGE}.")

if __name__ == "__main__":
    if app_config.STAGE == "dev":  # API runs on separate port
        import uvicorn

        uvicorn.run("main:app", host="0.0.0.0", port=8200, reload=True)
    else:
        import sys

        logger.error("App should only be executed directly in development stage.")
        sys.exit(1)

    # * in qa and prod uvicorn will be executed as command directly
    # // elif app_config.STAGE == "qa":  # API is behind nginx
    # //     logger.info(f"Running in stage qa on {app_config.HOST_URL}/api.")
    # //     uvicorn.run("main:app", host="0.0.0.0", port=8200, root_path="/api")
    # // else:  # API is behind nginx
    # //     logger.info(f"Running in stage prod on {app_config.HOST_URL}/api.")
    # //     uvicorn.run("main:app", host="0.0.0.0", port=8200, root_path="/api")
