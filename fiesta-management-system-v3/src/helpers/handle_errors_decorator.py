"""
Provides a decorator for handling responses in routers
"""

import functools
import traceback
import logging
from jsonschema import ValidationError
from fastapi import status
from fastapi.responses import JSONResponse
from src.helpers.exceptions import (
    LoginError,
    NoSuchUserError,
    NotFoundException,
    BadRequestException,
    NoMenuFoundError,
    error,
)


logger = logging.getLogger(__name__)


def handle_errors(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return_value = function(*args, **kwargs)
            return return_value

        except (NoSuchUserError, NotFoundException, NoMenuFoundError) as err:
            logger.error(str(err))
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=error(code=404, message=str(err)),
            )

        except LoginError as err:
            logger.error(str(err))
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=error(code=401, message=str(err)),
            )

        except BadRequestException as err:
            logger.error(str(err))
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=error(code=400, message=str(err)),
            )
        except ValidationError as err:
            logger.error(str(err))
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=error(code=400, message=str(err).split("\n")[0]),
            )

        except Exception as err:
            # logger.critical()
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=error(code=500, message=str(err)),
            )

    return wrapper
