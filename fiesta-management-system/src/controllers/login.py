import hashlib

from src.helpers.exceptions import NoSuchUserError
from src.models.database import Database
from src.utils import queries


class Login:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def authenticate_credentials(self):
        try:
            if self.authenticate_user():
                return True
            else:
                return False
        except NoSuchUserError:
            raise NoSuchUserError

    def authenticate_user(self):
        db = Database()
        db_hashed_password = db.get_item(queries.GET_HASHED_PASSWORD, (self.user_name,))
        hashed_password = self.get_hash()

        if db_hashed_password is None:
            raise NoSuchUserError
        elif db_hashed_password[0] == hashed_password:
            return True
        else:
            return False

    def get_hash(self):
        password = self.password.encode()
        pass_hash = hashlib.sha256(password).hexdigest()
        return pass_hash


if __name__ == "__main__":
    login_obj = Login("tgoyal", "Tusharpass1!")
    print(login_obj.get_user_details())
