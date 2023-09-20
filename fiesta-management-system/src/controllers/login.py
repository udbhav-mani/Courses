import hashlib

from src.helpers.exceptions import NoSuchUserError
from src.models.database import Database
from src.utils import config


class Login:
    def authenticate_credentials(self, user_name, password):
        try:
            if self.__authenticate_user(user_name, password):
                return True
            return False
        except NoSuchUserError:
            raise NoSuchUserError

    @staticmethod
    def __authenticate_user(user_name, password):
        db_hashed_password = Login.__get_password_from_db(user_name)
        hashed_password = Login.__get_hash(password)

        if db_hashed_password is None:
            raise NoSuchUserError
        elif db_hashed_password[0] == hashed_password:
            return True
        else:
            return False

    @staticmethod
    def __get_password_from_db(user_name):
        db = Database()
        db_hashed_password = db.get_item(config.queries["GET_HASHED_PASSWORD"], (user_name,))
        return db_hashed_password

    @staticmethod
    def __get_hash(password):
        password = password.encode()
        pass_hash = hashlib.sha256(password).hexdigest()
        return pass_hash
