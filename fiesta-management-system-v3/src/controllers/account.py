import logging
from src.models.database import Database
from src.utils import config
from src.helpers import log, NoSuchUserError


logger = logging.getLogger(__name__)


class Account:
    """
    Account class which deals with
    all the manipulations regarding balance of an employee
    """

    @log(logger=logger)
    def view_balance(self, user_id=None):
        db = Database()
        balance = db.get_item(config.queries["VIEW_BALANCE"], (user_id,))
        if balance:
            return balance[0]

        raise NoSuchUserError("No such user found!")

    @staticmethod
    @log(logger=logger)
    def update_balance(amount, grp_id=None, user_id=None):
        db = Database()
        if user_id is None:
            db.update_item(config.queries["UPDATE_BALANCE_GROUP"], (amount, grp_id))
        else:
            db.update_item(config.queries["UPDATE_BALANCE_USER"], (amount, user_id))
