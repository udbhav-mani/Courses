from src.helpers.jwt_helper import create_access_token
from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.exceptions import NoSuchUserError, error
from datetime import timedelta
from fastapi import (
    status,
    APIRouter,
    Response,
    Body,
)
from fastapi.responses import JSONResponse

from typing import Annotated

router = APIRouter()


@router.post("/login")
def post(response: Response, body: Annotated[dict, Body()]):
    user_data = body
    instance = Login()
    try:
        is_authenticated = instance.authenticate_credentials(
            user_name=user_data.get("username"), password=user_data.get("password")
        )
        if isinstance(is_authenticated, str):
            return error(code=404, message="No such user found")
    except NoSuchUserError:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=error(code=404, message="No such user found."),
        )
    else:
        if is_authenticated:
            user = User(user_name=user_data.get("username"))
            user.get_details()
            user_data = {
                "sub": user_data.get("username"),
                "user_id": user.user_id,
                "grp_id": user.grp_id,
                "role": user.role,
            }
            access_token = create_access_token(
                user_data, expires_delta=timedelta(minutes=20)
            )
            response.set_cookie(key="access_token", value=access_token, httponly=True)
            return {"access_token": access_token}
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error(code=401, message="Invalid credentials."),
            )
