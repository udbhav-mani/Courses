from src.controllers.account import Account
from src.controllers.criteria import Criteria
from src.controllers.feedback import Feedback
from src.controllers.menu import Menu
from src.controllers.orders import Orders
from src.models.database import Database


class User(Menu, Orders, Account, Feedback, Criteria):
    def __init__(self, user_name=None, user_id=None, grp_id=None, role=None):
        self.user_name = user_name
        self.user_id = user_id
        self.grp_id = grp_id
        self.role = role

    def get_details(self, user_name = None):
        db = Database()
        query = ("select a.id, a.user_name, r.role, u.grp_id from authentication as a inner join user_roles as r on ("
                 "a.id = r.user_id) inner join users as u on (u.user_id = a.id) where user_name = %s")
        response = db.get_items(query, (self.user_name,))
        print(response)
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
        query = "select user_id, balance from user_balance where grp_id=%s;"
        response = db.get_items(query, (grp_id,))
        if response is not None:
            return [dict(user_id=item[0], balance=item[1]) for item in response]



if __name__ == "__main__":
    user = User()
    resp = user.get_users(grp_id=1)
    print(resp)
