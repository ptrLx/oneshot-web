import uvicorn
from fastapi import FastAPI

from router.user import router as user_router
from router.login import router as login_router
from router.image import router as image_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(login_router, prefix="/login", tags=["Login"])
app.include_router(image_router, prefix="/image", tags=["Image"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
