from typing import Union

from fastapi import FastAPI
from app.helper.config import APP_DESCRIPTION, APP_NAME, APP_VERSION
from app.router.router import router as public_router

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

app.include_router(public_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
