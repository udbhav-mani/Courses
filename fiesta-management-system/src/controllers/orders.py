from src.models.database import Database
from src.utils import queries


class Orders:
    def place_order(self):
        balance = self.view_balance()
        if balance < 137:
            print("Low Balance, Contact admin or visit fiesta to Topup Card!")
        else:
            self.update_balance(user_id=self.user_id, amount=-137)
            self.store_order(
                user_id=self.user_id, amount=137, created_by=self.user_name
            )
            print("Order placed! Thank You!!")

    def store_order(self, user_id, amount, created_by):
        db = Database()
        db.add_item(queries.STORE_ORDER, (user_id, amount, created_by))

    def check_order(self):
        db = Database()
        response = db.get_item(queries.CHECK_ORDER, (self.user_id,))
        return response
