import logging
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
logger = logging.getLogger(__name__)


@router.post("/login", status_code=status.HTTP_200_OK)
def post(response: Response, body: Annotated[dict, Body()]):
    logger.debug(f"/login endpoint called for user -> {body.get('username')}")
    user_data = body
    instance = Login()
    try:
        is_authenticated = instance.authenticate_credentials(
            user_name=user_data.get("username"), password=user_data.get("password")
        )
        if isinstance(is_authenticated, str):
            logger.error(
                f"/login endpoint [error -> No such user found] -> {body.get('username')}"
            )
            return error(code=404, message="No such user found")
    except NoSuchUserError:
        logger.error(
            f"/login endpoint [error -> No such user found] -> {body.get('username')}"
        )
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
            logger.info(f"user logged in with data -> {user_data}")
            access_token = create_access_token(
                user_data, expires_delta=timedelta(minutes=20)
            )
            response.set_cookie(key="access_token", value=access_token, httponly=True)
            return {"access_token": access_token}
        else:
            f"/login endpoint [error -> Invalid credentials.] -> {body.get('username')}"
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error(code=401, message="Invalid credentials."),
            )
