from src.helpers.exceptions import NotFoundException
from src.models.database import Database
from src.utils import config


class Feedback:
    @staticmethod
    def view_all_feedbacks(grp_id):
        db = Database()
        response = db.get_items(config.queries["VIEW_FEEDBACK"], (grp_id,))
        return [
            dict(criteria=tup[0], feedback=tup[1], comments=tup[2]) for tup in response
        ]

    @staticmethod
    def get_menu_fdb_criterias(grp_id):
        db = Database()
        response = db.get_items(config.queries["GET_MENU_FDB_CRITERIAS"], (grp_id,))
        if len(response) > 0:
            criterias = [{"cr_id": tup[1], "criteria": tup[2]} for tup in response]
            return criterias

        raise NotFoundException("No criterias have been decided for current menu.")

    @staticmethod
    def add_feedback(feedback):
        db = Database()
        db.add_items(config.queries["ADD_FEEDBACK"], feedback)
