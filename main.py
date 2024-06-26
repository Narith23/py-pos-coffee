from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.helper.config import APP_DESCRIPTION, APP_NAME, APP_VERSION
from app.router.router import router as public_router

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates directory admin
admin = Jinja2Templates(directory="templates/admin")

# Initialize Jinja2 templates directory client
client = Jinja2Templates(directory="templates/client")

app.include_router(public_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
