import functools
from helpers.validators import Validators
from src.helpers.jwt_helper import get_token
from fastapi import status
from fastapi.responses import JSONResponse
from src.helpers.exceptions import error


def grant_access(roles_allowed: list):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            request = kwargs.get("request")
            token = get_token(request=request)
            role = token.get("role")
            if role in roles_allowed:
                return fun(*args, **kwargs)
            else:
                return JSONResponse(
                    status_code=status.HTTP_403_FORBIDDEN,
                    content=error(
                        code=403,
                        message="You do not have the permissions to perform this action.",
                    ),
                )

        return wrapper

    return decorator


def validate_body(schema):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            body = kwargs.get("body")
            validator = Validators.validate_request(schema, body)
            if validator:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content=error(code=404, message=validator.split("\n")[0]),
                )
            else:
                return fun(*args, **kwargs)

        return wrapper

    return decorator
