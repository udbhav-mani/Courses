import functools
from src.helpers import get_logger



def log(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        operation = fun.__name__
        args_repr = [repr(item) for item in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"{operation} called with {signature}.")
        val = fun(*args, **kwargs)
        logger.debug(f"{operation} returned {val}.")
        return val

    return wrapper
