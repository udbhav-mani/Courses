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
        # Menu.display_menu(response)

    def propose_menu(self, data, date, name, grp_id):
        db = Database()
        query_add_menu = (
            "insert into menu(date,status,created_by, grp_id) values(%s,%s,%s,%s);"
        )
        query_propose_items = "insert into items(menu_id, items) values(%s,%s)"
        data_tuple = (date, "pending", name, grp_id)
        _id = db.add_item(query_add_menu, data_tuple)
        data_list = [(_id, item) for item in data]
        db.add_items(query_propose_items, data_list)
        return "success"

    def reject_menu(self, menu_id, comments, username):
        try:
            db = Database()
            self.update_menu_status("rejected", menu_id)
            data_tuple = (menu_id, comments, username)
            db.add_item(config.queries["QUERY_ADD_COMMENT"], data_tuple)
        except Exception as error:
            return f"error - {error.__str__()}"
        else:
            return "success"

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
        data_tuple = (
            status,
            menu_id,
        )
        query = "update menu set status = %s where id = %s"
        db.update_item(query, data_tuple)
        return "success"

    def update_menu(self, menu_id, old_item, new_item):
        db = Database()
        db.update_item(config.queries["UPDATE_ITEM"], (new_item, old_item, menu_id))
        self.update_menu_status(status="pending", menu_id=menu_id)
