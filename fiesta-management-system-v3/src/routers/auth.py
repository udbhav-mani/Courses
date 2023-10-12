"""
FastAPI route for user login, which authenticates the user's credentials,
generates an access token, and returns.
"""
from datetime import timedelta
import logging
from typing import Annotated
from fastapi import (
    status,
    APIRouter,
    Response,
    Body,
)

from src.controllers import Login, User
from src.helpers import create_access_token, log, handle_errors

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
@log(logger=logger)
@handle_errors
def login(response: Response, body: Annotated[dict, Body()]):
    """
    Authenticates user credentials and returns an access token.

    Args:
      response (Response): FASTAPI response abject
      body (Annotated[dict, Body()])

    Returns:
    "access_token" and "token_type".
    """
    instance = Login()
    instance.authenticate_credentials(
        user_name=body.get("username"), password=body.get("password")
    )
    jwt = __get_access_token(body)
    return {"access_token": jwt, "token_type": "bearer"}


def __get_access_token(user_data):
    """
    Generates an access token for a user based on their username and
    user details.
    """
    user = User(user_name=user_data.get("username"))
    user.get_details()
    user_data = {
        "sub": user_data.get("username"),
        "user_id": user.user_id,
        "grp_id": user.grp_id,
        "role": user.role,
    }
    access_token = create_access_token(user_data, expires_delta=timedelta(minutes=20))
    return access_token
