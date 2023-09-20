from prettytable import PrettyTable

from src.helpers.decorators import restrict_access
from src.helpers.exceptions import NoMenuFoundError
from src.models.database import Database
from src.utils import config


class Menu:

    def view_accepted_menu(self):
        db = Database()
        data_tuple = (self.grp_id,)
        response = db.get_items(config.queries["GET_ACCEPTED_MENU"], data_tuple)
        Menu.display_menu(response)

    def propose_menu(self, data, date):
        db = Database()
        data_tuple = (date, "pending", self.user_name, self.grp_id)
        _id = db.add_item(config.queries["ADD_MENU"], data_tuple)
        data_list = [(_id, item) for item in data]
        db.add_items(config.queries["PROPOSE_MENU_ITEMS"], data_list)
        return "Menu has been added!! "

    def reject_menu(self, menu_id, comments):
        db = Database()
        data_tuple = (menu_id,)
        db.update_item(config.queries["REJECT_MENU"], data_tuple)

        data_tuple = (menu_id, comments, self.user_name)
        db.add_item(config.queries["QUERY_ADD_COMMENT"], data_tuple)

    def get_pending_menu(self):
        db = Database()
        data_tuple = ("pending", self.grp_id)
        response = db.get_items(config.queries["GET_MENU"], data_tuple)
        return response

    def get_not_published_menu(self):
        db = Database()
        items = db.get_items(config.queries["GET_MENU"], ("not published", self.grp_id))
        return items

    def publish_menu(self, _menu_id, _menu_date):
        db = Database()
        data_tuple = (_menu_id,)
        db.update_item(config.queries["QUERY_MENU_STATUS"], data_tuple)

        data_tuple = (_menu_id, _menu_date)
        _id = db.add_item(config.queries["QUERY_APPROVE_MENU"], data_tuple)

        data_tuple = (_id, self.grp_id)
        db.update_item(config.queries["QUERY_UPDATE_GROUP"], data_tuple)
        self.update_balance(amount=137, grp_id=self.grp_id)

    def check_menu_status(self, status):
        db = Database()
        response = db.get_item(config.queries["CHECK_MENU_STATUS"], (status, self.grp_id))
        return response

    def check_rejected_menu(self):
        db = Database()
        response = db.get_item(config.queries["CHECK_REJECTED_MENU"], (self.grp_id,))
        return response

    @staticmethod
    def discard_menu(data):
        db = Database()
        db.update_item(config.queries["DISCARD_MENU"], (data,))

    @staticmethod
    def update_menu(menu_id, old_item, new_item):
        db = Database()
        db.update_item(config.queries["UPDATE_ITEM"], (new_item, old_item, menu_id))
        db.update_item(config.queries["UPDATE_MENU"], (menu_id,))

    @staticmethod
    def view_menu(_menu_id):
        db = Database()
        data_tuple = (_menu_id,)
        response = db.get_items(config.queries["VIEW_MENU_BY_MENUID"], data_tuple)
        Menu.display_menu(response)
        return response

    @staticmethod
    def display_menu(data):
        try:
            date = data[0][1]
        except NoMenuFoundError:
            raise NoMenuFoundError
        else:
            table = PrettyTable(["Item number", "Item"])
            table.title = f"Menu ({date})"
            items = [tup[0] for tup in data]
            for index, item in enumerate(items, start=1):
                table.add_row([f"{index}", f"{item}"])

            print(f"\n{table}\n")

    @staticmethod
    def accept_menu(menu_id):
        db = Database()
        data_tuple = (menu_id,)
        db.update_item(config.queries["ACCEPT_MENU"], data_tuple)


if __name__ == "__main__":
    menu = Menu()
    resp = menu.view_menu(17)
