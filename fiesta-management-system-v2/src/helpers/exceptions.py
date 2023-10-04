from src.utils.config import error_response


class NoSuchUserError(LookupError):
    pass


class NoMenuFoundError(Exception):
    pass


class AccessDeniedException(Exception):
    pass


class DbException(Exception):
    pass


def error(code=None, message=None):
    error_response["error"]["code"] = code
    error_response["error"]["message"] = message
    return error_response, code
