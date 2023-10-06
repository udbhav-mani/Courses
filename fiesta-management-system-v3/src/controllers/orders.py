from src.models.database import Database
from src.utils import config


class Orders:

    def check_order(self, user_id=None, date=None):
        db = Database()
        response = db.get_items(config.queries["CHECK_ORDER"], (user_id,))
        if date is None:
            return [dict(order_id=item[0], user_id=item[1], amount=item[2], date=str(item[3])[:10]) for item in
                    response]
        else:
            return [dict(order_id=item[0], user_id=item[1], amount=item[2], date=str(item[3])[:10])
                    for item in response
                    if str(item[3])[:10] == date]

    @staticmethod
    def store_order(user_id, amount, created_by):
        db = Database()
        order_id = db.add_item(config.queries["STORE_ORDER"],
                               (user_id, amount, created_by))
        return order_id
