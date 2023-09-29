from src.models.database import Database


class Orders:

    def check_order(self, user_id=None, date=None):
        db = Database()
        query = "select id, user_id, amount, created_at from orders where user_id = %s order by created_at desc;"
        response = db.get_items(query, (user_id,))
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
        order_id = db.add_item("insert into orders(user_id, amount, created_by) values(%s,%s,%s)",
                               (user_id, amount, created_by))
        return order_id
