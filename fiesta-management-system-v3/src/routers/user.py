from fastapi import (
    status,
    APIRouter,
    Request,
    Query,
)
from fastapi.responses import JSONResponse
from typing import Annotated

from src.helpers.jwt_helper import get_token
from src.controllers.user import User
from src.helpers.exceptions import error

router = APIRouter()


@router.get("/users", status_code=status.HTTP_200_OK)
def get_users(request: Request, user_id: Annotated[int | None, Query()] = None):
    grp_id = get_token(request).get("grp_id")

    user = User()
    response = user.get_users(grp_id=grp_id)
    if user_id is not None:
        for item in response:
            if item.get("user_id") == user_id:
                return [item]

        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=error(code=404, message="No such user found."),
        )
    else:
        return response
