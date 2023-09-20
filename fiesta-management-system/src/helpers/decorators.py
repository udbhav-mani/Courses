from src.helpers.exceptions import AccessDeniedException


def restrict_access(params):
    def my_decorator(func):
        def access_specifier(*args, **kwargs):
            role = args[0].role
            if role in params:
                func(*args, **kwargs)
            else:
                raise AccessDeniedException(
                    "You dont have the access to perform the following action!! "
                )

        return access_specifier
    return my_decorator
