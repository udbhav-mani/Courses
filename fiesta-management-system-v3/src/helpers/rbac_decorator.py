import functools
from fastapi import status
from fastapi.responses import JSONResponse

from src.helpers.exceptions import error
from src.helpers.jwt_helper import get_token
from src.utils.config import rbac as access_control_list, prompts


def grant_access(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        request = kwargs.get("request")
        token = get_token(request=request)
        role = token.get("role")
        operation = fun.__name__
        if operation in access_control_list.get(role):
            return fun(*args, **kwargs)

        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=error(
                code=403,
                message= prompts.get("PERMISSION_DENIED"),
            ),
        )

    return wrapper
