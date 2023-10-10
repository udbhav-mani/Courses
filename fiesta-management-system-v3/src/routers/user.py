import logging
from fastapi import (
    status,
    APIRouter,
    Request,
    Query,
)
from typing import Annotated

from src.controllers import User
from src.helpers import log, handle_errors, get_token, NoSuchUserError

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK)
@handle_errors
@log(logger=logger)
def get_users(request: Request, user_id: Annotated[int | None, Query()] = None):
    grp_id = get_token(request).get("grp_id")

    user = User()
    response = user.get_users(grp_id=grp_id)

    if not user_id:
        return response

    for item in response:
        if item.get("user_id") == user_id:
            return [item]
    raise NoSuchUserError("No such user found.")
