class NoSuchUserError(LookupError):
    pass


class NoMenuFoundError(Exception):
    pass


class AccessDeniedException(Exception):
    pass


class DbException(Exception):
    pass
