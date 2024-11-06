from fastapi import APIRouter

from settings.config import settings
from app.authentication.fastapiusers import fastapi_users
from app.authentication.dependencies import authentication_backend
from schemas.user import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Аутентификация"],
)

router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True,
    ),
)

router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
