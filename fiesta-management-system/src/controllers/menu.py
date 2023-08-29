from prettytable import PrettyTable
from src.helpers.exceptions import NoMenuFoundError
from src.models.database import Database
from src.utils import queries


class Menu:
    def view_menu(self, _menu_id):
        db = Database()
        data_tuple = (_menu_id,)
        response = db.get_items(queries.VIEW_MENU_BY_MENUID, data_tuple)
        Menu.display_menu(response)
        return response

    def view_accepted_menu(self):
        db = Database()
        data_tuple = (self.grp_id,)
        response = db.get_items(queries.GET_ACCEPTED_MENU, data_tuple)
        Menu.display_menu(response)

    def propose_menu(self, data, date):
        db = Database()
        data_tuple = (date, "pending", self.user_name, self.grp_id)
        _id = db.add_item(queries.ADD_MENU, data_tuple)
        data_list = [(_id, item) for item in data]
        db.add_items(queries.PROPOSE_MENU_ITEMS, data_list)
        print("Menu has been added!! ")

    @staticmethod
    def accept_menu(menu_id):
        db = Database()
        data_tuple = (menu_id,)
        db.update_item(queries.ACCEPT_MENU, data_tuple)

    def reject_menu(self, menu_id, comments):
        db = Database()
        data_tuple = (menu_id,)
        db.update_item(queries.REJECT_MENU, data_tuple)

        data_tuple = (menu_id, comments, self.user_name)
        db.add_item(queries.QUERY_ADD_COMMENT, data_tuple)

    def discard_menu(self, data):
        db = Database()
        db.update_item(queries.DISCARD_MENU, (data,))

    def get_pending_menu(self):
        db = Database()
        data_tuple = ("pending", self.grp_id)
        response = db.get_items(queries.GET_MENU, data_tuple)
        return response

    def get_npublished_menu(self):
        db = Database()
        items = db.get_items(queries.GET_MENU, ("not published", self.grp_id))
        return items

    def publish_menu(self, _menu_id, _menu_date):
        db = Database()
        data_tuple = (_menu_id,)
        db.update_item(queries.QUERY_MENU_STATUS, data_tuple)

        data_tuple = (_menu_id, _menu_date)
        _id = db.add_item(queries.QUERY_APPROVE_MENU, data_tuple)

        data_tuple = (_id, self.grp_id)
        db.update_item(queries.QUERY_UPDATE_GROUP, data_tuple)
        self.update_balance(amount=137, grp_id=self.grp_id)

    def check_menu_status(self, status):
        db = Database()
        response = db.get_item(queries.CHECK_MENU_STATUS, (status, self.grp_id))
        return response

    def update_menu(self, menu_id, old_item, new_item):
        db = Database()
        db.update_item(queries.UPDATE_ITEM, (new_item, old_item, menu_id))
        db.update_item(queries.UPDATE_MENU, (menu_id,))

    @staticmethod
    def display_menu(data):
        try:
            date = data[0][1]
        except:
            raise NoMenuFoundError
        else:
            print(f"Date of menu -> {date}.")
            t = PrettyTable(["Item number", "Item"])
            t.title = f"Menu"
            items = [tup[0] for tup in data]
            for index, item in enumerate(items, start=1):
                t.add_row([f"{index}", f"{item}"])
            print(t)


if __name__ == "__main__":
    menu = Menu()
    resp = menu.view_menu(17)
