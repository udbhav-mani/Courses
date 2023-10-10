from src.helpers.exceptions import NoSuchUserError
from src.controllers.account import Account
from src.controllers.criteria import Criteria
from src.controllers.feedback import Feedback
from src.controllers.menu import Menu
from src.controllers.orders import Orders
from src.models.database import Database
from src.utils import config


class User(Menu, Orders, Account, Feedback, Criteria):
    def __init__(self, user_name=None, user_id=None, grp_id=None, role=None):
        self.user_name = user_name
        self.user_id = user_id
        self.grp_id = grp_id
        self.role = role

    def get_details(self, user_name=None):
        db = Database()
        response = db.get_items(config.queries["GET_DETAILS"], (self.user_name,))
        # print(response)
        data = dict(
            user_id=response[0][0],
            user_name=response[0][1],
            role=response[0][2],
            grp_id=response[0][3],
        )
        self.user_id = data["user_id"]
        self.grp_id = data["grp_id"]
        self.role = data["role"]

    def get_users(self, grp_id):
        db = Database()
        response = db.get_items(config.queries["GET_USERS"], (grp_id,))
        if response:
            return [dict(user_id=item[0], balance=item[1]) for item in response]
        raise NoSuchUserError("Couldn't get users.")
