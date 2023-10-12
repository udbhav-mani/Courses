"""
Contains all exceptions and error related classes and methods
"""
from src.utils.config import error_response


class NoSuchUserError(LookupError):
    """Raised when a user is not found"""


class LoginError(LookupError):
    """Raised when an error occurs at time of login"""


class NoMenuFoundError(Exception):
    """Raised when a menu is not found"""


class AccessDeniedException(Exception):
    """Raised when access is denied"""


class DbException(Exception):
    """Raised when db calls raises an error"""


class NotFoundException(Exception):
    """Raised when something us not found"""


class BadRequestException(Exception):
    """Raised when user gives a bad request"""


def error(code=None, message=None):
    """formats and returns the error according to code and message"""
    error_response["error"]["code"] = code
    error_response["error"]["message"] = message
    return error_response
