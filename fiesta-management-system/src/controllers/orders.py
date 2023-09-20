from src.models.database import Database
from src.utils import config


class Orders:
    def place_order(self):
        balance = self.view_balance()
        if balance < 137:
            return -1
        else:
            self.update_balance(user_id=self.user_id, amount=-137)
            self.store_order(
                user_id=self.user_id, amount=137, created_by=self.user_name
            )
            return balance - 137

    def check_order(self):
        db = Database()
        response = db.get_item(config.queries["CHECK_ORDER"], (self.user_id,))
        return response

    @staticmethod
    def store_order(user_id, amount, created_by):
        db = Database()
        db.add_item(config.queries["STORE_ORDER"], (user_id, amount, created_by))
