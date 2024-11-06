from fastapi import APIRouter

from settings.config import settings
from app.authentication.fastapiusers import fastapi_users
from schemas.user import (
    UserRead,
    UserUpdate,
)

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Пользователи"],
)

router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
