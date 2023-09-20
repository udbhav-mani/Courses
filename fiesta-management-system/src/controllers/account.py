from src.models.database import Database
from src.utils import config


class Account:
    """
    Account class which deals with
    all the manipulations regarding balance of an employee
    """
    def view_balance(self, user_id=None):
        if user_id is None:
            user_id = self.user_id

        db = Database()
        balance = db.get_item(config.queries["VIEW_BALANCE"], (user_id,))
        return balance[0]

    @staticmethod
    def update_balance(amount, grp_id=None, user_id=None):
        db = Database()
        if user_id is None:
            db.update_item(config.queries["UPDATE_BALANCE_GROUP"], (amount, grp_id))
        else:
            db.update_item(config.queries["UPDATE_BALANCE_USER"], (amount, user_id))
