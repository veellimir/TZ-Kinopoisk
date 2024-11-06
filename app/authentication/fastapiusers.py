from fastapi_users import FastAPIUsers

from app.users.models import User
from app.authentication.dependencies import get_user_manager
from app.authentication.dependencies import authentication_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)
