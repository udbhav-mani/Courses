from src.models.database import Database
from src.utils import queries


class Feedback:
    def view_all_feedbacks(self):
        db = Database()
        response = db.get_items(queries.VIEW_FEEDBACK, (self.grp_id,))
        return response

    def get_menu_fdb_criterias(self):
        db = Database()
        response = db.get_items(queries.GET_MENU_FDB_CRITERIAS, (self.grp_id,))
        if len(response) > 0:
            criterias = [
                {"menu_id": tup[0], "cr_id": tup[1], "criteria": tup[2]}
                for tup in response
            ]
            return criterias
        else:
            return None

    def check_user_feedback(self):
        db = Database()
        response = db.get_item(queries.CHECK_USER_FDB, (self.user_id,))
        if response is None:
            return False
        else:
            return True

    @staticmethod
    def add_feedback(feedback):
        db = Database()
        db.add_items(queries.ADD_FEEDBACK, feedback)
