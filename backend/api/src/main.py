import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.user import router as user_router
from router.login import router as login_router
from router.image import router as image_router


app = FastAPI()

origins = ["http://localhost:8100"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(login_router, prefix="/login", tags=["Login"])
app.include_router(image_router, prefix="/image", tags=["Image"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8200, reload=True)
