"""
Defines class Account for functions related to account
"""
import logging
from src.models.database import Database
from src.utils import config
from src.helpers import log, NoSuchUserError


logger = logging.getLogger(__name__)


class Account:
    """
    Provides methods for viewing and updating account balances.
    """

    @log(logger=logger)
    def view_balance(self, user_id=None):
        """
        Retrieves the balance of a user from a database and returns it, or
        raises an error if the user does not exist.

        Args:
          user_id (int): user_id of user

        Returns:
          The balance of the user.
        """
        db = Database()
        balance = db.get_item(config.queries["VIEW_BALANCE"], (user_id,))
        if balance:
            return balance[0]

        raise NoSuchUserError("No such user found!")

    @staticmethod
    @log(logger=logger)
    def update_balance(amount, grp_id=None, user_id=None):
        """
        Updates the balance of either a group or a user in a database.

        Args:
          amount: the amount to be updated.
          grp_id: grp_id
          user_id: user_id of user
        """
        db = Database()
        if user_id is None:
            db.update_item(config.queries["UPDATE_BALANCE_GROUP"], (amount, grp_id))
        else:
            db.update_item(config.queries["UPDATE_BALANCE_USER"], (amount, user_id))
