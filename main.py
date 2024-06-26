from typing import Union

from fastapi import FastAPI
from app.router.router import router as public_router

app = FastAPI()

app.include_router(public_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
