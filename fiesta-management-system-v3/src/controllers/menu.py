from src.models.database import Database
from src.utils import config


class Menu:
    @staticmethod
    def get_menu_from_group(grp_id):
        db = Database()
        response = db.get_item(
            config.queries["SET_FEEDBACK_CRITERIA_QUERY1"], (grp_id,)
        )
        _menu_id = response[0]
        return _menu_id

    def view_accepted_menu(self, grp_id):
        db = Database()
        data_tuple = (grp_id,)
        response = db.get_items(config.queries["GET_ACCEPTED_MENU"], data_tuple)
        return response

    def propose_menu(self, data, date, name, grp_id):
        db = Database()
        data_tuple = (date, "pending", name, grp_id)
        _id = db.add_item(config.queries["ADD_MENU"], data_tuple)
        data_list = [(_id, item) for item in data]
        db.add_items(config.queries["PROPOSE_MENU_ITEMS"], data_list)

    def reject_menu(self, menu_id, comments, username):
        db = Database()
        self.update_menu_status("rejected", menu_id)
        data_tuple = (menu_id, comments, username)
        db.add_item(config.queries["QUERY_ADD_COMMENT"], data_tuple)

    def get_menu_by_status(self, grp_id, status):
        db = Database()
        items = db.get_items(config.queries["GET_MENU"], (status, grp_id))
        return items

    def publish_menu(self, menu_id, menu_date, grp_id):
        db = Database()
        self.update_menu_status("published", menu_id)

        data_tuple = (menu_id, menu_date)
        _id = db.add_item(config.queries["QUERY_APPROVE_MENU"], data_tuple)

        data_tuple = (_id, grp_id)
        db.update_item(config.queries["QUERY_UPDATE_GROUP"], data_tuple)

    def update_menu_status(self, status, menu_id):
        db = Database()
        db.update_item(config.queries["UPDATE_MENU_STATUS"], (status, menu_id))

    def update_menu(self, menu_id, old_item, new_item):
        db = Database()
        db.update_item(config.queries["UPDATE_ITEM"], (new_item, old_item, menu_id))
        self.update_menu_status(status="pending", menu_id=menu_id)
