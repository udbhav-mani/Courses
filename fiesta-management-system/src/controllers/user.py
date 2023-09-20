from src.controllers.account import Account
from src.controllers.criteria import Criteria
from src.controllers.feedback import Feedback
from src.controllers.menu import Menu
from src.controllers.orders import Orders
from src.models.database import Database
from src.utils import config


class User(Menu, Orders, Account, Feedback, Criteria):
    def __init__(self, user_name, user_id=None, grp_id=None, role=None):
        self.user_name = user_name
        self.user_id = user_id
        self.grp_id = grp_id
        self.role = role

    def get_details(self):
        db = Database()
        response = db.get_items(config.queries["GET_DETAILS"], (self.user_name,))
        data = dict(
            user_id=response[0][0],
            user_name=response[0][1],
            role=response[0][2],
            grp_id=response[0][3],
        )
        self.user_id = data["user_id"]
        self.grp_id = data["grp_id"]
        self.role = data["role"]

    def validate_user(self, user_id):
        db = Database()
        response = db.get_item(config.queries["VALIDATE_USER"], (user_id, self.grp_id))
        if response is not None:
            return True

        return False
