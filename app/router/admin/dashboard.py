from fastapi import APIRouter, Depends, Request, status
from fastapi.templating import Jinja2Templates

from app.router.auth.auth import TokenData
from app.router.auth.verify_token import get_web_user


router = APIRouter(prefix="/dashboard")

dashboard = Jinja2Templates(directory="templates/admin/dashboard")


@router.get("", status_code=status.HTTP_200_OK)
async def get_dashboard(request: Request, user: TokenData = Depends(get_web_user)):
    return dashboard.TemplateResponse("dashboard.html", {"request": request})
