"""
Provides a class which provides all the operations
related to menu
"""
from src.models.database import Database
from src.utils import config
from src.helpers import NoMenuFoundError


class Menu:
    """
    Provides methods for managing menus, viewing accepted menus,
    proposing menus, rejecting menus, getting menus by status,
    publishing menus, and updating menus.
    """

    @staticmethod
    def get_menu_from_group(grp_id):
        """
        Retrieves menuId for a grp.

        Args:
        grp_id: grp_id

        Returns:
        - menu_id
        """
        db = Database()
        response = db.get_item(
            config.queries["SET_FEEDBACK_CRITERIA_QUERY1"], (grp_id,)
        )
        _menu_id = response[0]
        return _menu_id

    def view_accepted_menu(self, grp_id):
        """
        Retrieves the accepted menu items.

        Args:
        grp_id: grp_id of a person.

        Returns:
        the items from the accepted menu.
        """
        db = Database()
        data_tuple = (grp_id,)
        items = db.get_items(config.queries["GET_ACCEPTED_MENU"], data_tuple)
        if items:
            return items
        raise NoMenuFoundError("No such menu found!")

    def propose_menu(self, data, date, name, grp_id):
        """
        Add a new menu to the menu table,
        waiting to be approved.

        Args:
        data: items of the menu
        date: date of menu
        name: name of the person proposing menu
        grp_id: grp_id of the menu
        """
        db = Database()
        data_tuple = (date, "pending", name, grp_id)
        _id = db.add_item(config.queries["ADD_MENU"], data_tuple)
        data_list = [(_id, item) for item in data]
        db.add_items(config.queries["PROPOSE_MENU_ITEMS"], data_list)

    def reject_menu(self, menu_id, comments, username):
        """
        Reject a menu by f_emp.

        Args:
        menu_id: menu_id of the menu
        comments: comments for rejection
        username: name of the person rejecting menu
        """
        db = Database()
        self.update_menu_status("rejected", menu_id)
        data_tuple = (menu_id, comments, username)
        db.add_item(config.queries["QUERY_ADD_COMMENT"], data_tuple)

    def get_menu_by_status(self, grp_id, status):
        """
        Retrieves any menu by status.

        Args:
        grp_id: grp_id of a person.
        status: status of the menu to be displayed.

        Returns:
        the items from the accepted menu.
        """
        db = Database()
        items = db.get_items(config.queries["GET_MENU"], (status, grp_id))
        if items:
            return items

        raise NoMenuFoundError("No such menu found!")

    def publish_menu(self, menu_id, menu_date, grp_id):
        """
        Publish the menu to the group

        Args:
        menu_id: menu_id of the menu to be published.
        grp_id: grp_id of a person.
        menu_date: date of the menu to be published.
        """
        db = Database()
        self.update_menu_status("published", menu_id)

        data_tuple = (menu_id, menu_date)
        _id = db.add_item(config.queries["QUERY_APPROVE_MENU"], data_tuple)

        data_tuple = (_id, grp_id)
        db.update_item(config.queries["QUERY_UPDATE_GROUP"], data_tuple)

    def update_menu_status(self, status, menu_id):
        """
        Update the menu status

        Args:
        status: status of the menu to be updated.
        menu_id: menu_id of the menu to be updated.
        """
        db = Database()
        db.update_item(config.queries["UPDATE_MENU_STATUS"], (status, menu_id))

    def update_menu(self, menu_id, old_item, new_item):
        """
        Update the menu item by menu_id

        Args:
        old_item: name of the item to be updated.
        new_item: new item to be added.
        menu_id: menu_id of the menu to be updated.
        """
        db = Database()
        rid = db.update_item(
            config.queries["UPDATE_ITEM"], (new_item, old_item, menu_id)
        )
        if not rid:
            raise NoMenuFoundError("Could not update, No such menu or item found!")
        self.update_menu_status(status="pending", menu_id=menu_id)
