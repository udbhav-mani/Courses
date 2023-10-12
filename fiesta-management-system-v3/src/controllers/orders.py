"""
Provides a class for operations related to orders
"""

from src.models.database import Database
from src.utils import config


class Orders:
    """
    Provides methods for checking and storing orders in a database.
    """

    def check_order(self, user_id=None, date=None):
        """
        Retrieves order information

        Args:
          user_id: user_id .
          date: date (optional) for filtering.

        Returns:
        - List of dictionaries
        - Each dictionary represents an order
        - "order_id", "user_id", "amount", and "date".
        """
        db = Database()
        response = db.get_items(config.queries["CHECK_ORDER"], (user_id,))
        if date is None:
            return [
                {
                    "order_id": item[0],
                    "user_id": item[1],
                    "amount": item[2],
                    "date": str(item[3])[:10],
                }
                for item in response
            ]

        return [
            {
                "order_id": item[0],
                "user_id": item[1],
                "amount": item[2],
                "date": str(item[3])[:10],
            }
            for item in response
            if str(item[3])[:10] == date
        ]

    @staticmethod
    def store_order(user_id, amount, created_by):
        """
        Stores an order in a database.

        Args:
          user_id: Tuser_id
          amount: total amount of order
          created_by: name of person which created the order

        Returns:
        - order_id.
        """
        db = Database()
        order_id = db.add_item(
            config.queries["STORE_ORDER"], (user_id, amount, created_by)
        )
        return order_id
