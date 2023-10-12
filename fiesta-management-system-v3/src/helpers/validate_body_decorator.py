import functools
from fastapi import status
from fastapi.responses import JSONResponse

from src.helpers.validators import Validators
from src.helpers.exceptions import error


def validate_body(schema):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            body = kwargs.get("body")
            validator = Validators.validate_request(schema, body)
            if validator:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content=error(code=404, message= validator.split('\n', maxsplit=1)[0][0]),
                )
            return fun(*args, **kwargs)

        return wrapper

    return decorator
