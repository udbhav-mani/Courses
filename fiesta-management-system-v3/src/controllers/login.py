"""
Provides a class which provides all the operations
related to log in
"""
import hashlib

from src.helpers.exceptions import LoginError
from src.models.database import db
from src.utils import config


class Login:
    """
    Contains all the functionalities and methods for
    authenticating a user"""

    def authenticate_credentials(self, user_name, password):
        """
        Authenticate user credentials.

        Args:
          user_name: The username of the user trying to authenticate.
          password: The password of the user trying to authenticate.
        """
        try:
            self.__authenticate_user(user_name, password)
        except LoginError as err:
            raise LoginError(str(err)) from err

    @staticmethod
    def __authenticate_user(user_name, password):
        """
        Checks if the provided username and password match the hashed
        password stored in the database.

        Args:
          user_name: The username of the user trying to authenticate.
          password: The password of the user trying to authenticate.

        Returns:
          True if the user is authenticated successfully.
        """
        db_hashed_password = Login.__get_password_from_db(user_name)
        hashed_password = Login.__get_hash(password)

        if db_hashed_password is None:
            raise LoginError("No such user found!!")

        if db_hashed_password[0] == hashed_password:
            return True

        raise LoginError("Invalid Credentials")

    @staticmethod
    def __get_password_from_db(user_name):
        """
        Retrieves the hashed password for a given user name from a
        database.
        """
        db_hashed_password = db.get_item(
            config.queries["GET_HASHED_PASSWORD"], (user_name,)
        )
        return db_hashed_password

    @staticmethod
    def __get_hash(password):
        """
        Takes a password as input, encodes it, computes its SHA-256 hash, and returns the
        hash value.
        """
        password = password.encode()
        pass_hash = hashlib.sha256(password).hexdigest()
        return pass_hash
