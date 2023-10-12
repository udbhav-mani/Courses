"""
FastAPI endpoint that retrieves a list of users and optionally filters by
user ID.
"""
from typing import Annotated
import logging
from fastapi import (
    status,
    APIRouter,
    Request,
    Query,
)

from src.controllers import User
from src.helpers import log, handle_errors, get_token, NoSuchUserError
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK)
@handle_errors
@log(logger=logger)
def get_users(request: Request, user_id: Annotated[int | None, Query()] = None):
    """
    Retrieves a list of users based on the group ID and optionally filters the
    result by a specific user ID.

    Args:
      request (Request): FASTAPI request abject
      user_id (Annotated[int | None, Query()]): user_id of user

    Returns:
    Details of all users
    """
    grp_id = get_token(request).get("grp_id")

    user = User()
    response = user.get_users(grp_id=grp_id)

    if not user_id:
        return response

    for item in response:
        if item.get("user_id") == user_id:
            return [item]
    raise NoSuchUserError(prompts.get("NO_USER_FOUND"))
