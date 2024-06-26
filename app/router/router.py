from fastapi import APIRouter

# admin
from app.router.admin.user import router as admin_user_router
from app.router.admin.categories import router as admin_categories_router
from app.router.admin.products import router as admin_products_router
# client
from app.router.client.user import router as client_user_router
# auth
from app.router.auth.auth import router as auth_router

router = APIRouter(
    prefix="/api",
)

# admin
router.include_router(admin_user_router, prefix="/admin", tags=["admin user".upper()])
router.include_router(admin_categories_router, prefix="/admin", tags=["admin categories".upper()])
router.include_router(admin_products_router, prefix="/admin", tags=["admin products".upper()])
# client
router.include_router(client_user_router, prefix="/client", tags=["client"])
# auth
router.include_router(auth_router, prefix="/auth", tags=["auth".upper()])
