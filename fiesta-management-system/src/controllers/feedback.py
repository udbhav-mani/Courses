from prettytable import PrettyTable
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

    def get_fdb_criteria(self):
        db = Database()
        response = db.get_items(queries.GET_FDB_CRITERIAS)
        criteria = [line[0] for line in response]
        return criteria

    def add_new_criteria(self, new_criteria):
        db = Database()
        data_tuple = [(criteria,) for criteria in new_criteria]
        db.add_items(queries.UPDATE_CRITERIA, data_tuple)

    def set_fdb_criteria(self, criterias_selected):
        db = Database()
        response = db.get_item(queries.SET_FEEDBACK_CRITERIA_QUERY1, (self.grp_id,))
        _menu_id = response[0]
        cr_id_list = list()

        for criteria in criterias_selected:
            response = db.get_item(queries.SET_FEEDBACK_CRITERIA_QUERY2, (criteria,))
            _cr_id = response[0]
            cr_id_list.append(_cr_id)

        data_list = [(_menu_id, cr_id) for cr_id in cr_id_list]
        # print(data_list)

        db.add_items(queries.SET_FEEDBACK_CRITERIA_QUERY3, data_list)

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

    @staticmethod
    def display_criteria(data):
        t = PrettyTable(["S No.", "Criteria"])
        t.title = f"Criteria List"
        for index, item in enumerate(data, start=1):
            t.add_row([f"{index}", f"{item}"])
        print(t)


if __name__ == "__main__":
    fdb_obj = Feedback()
    fdb_obj.set_fdb_criteria()
