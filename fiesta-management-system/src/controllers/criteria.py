from prettytable import PrettyTable

from src.models.database import Database
from src.utils import config


class Criteria:
    def set_fdb_criteria(self, criterias_selected):
        db = Database()
        response = db.get_item(config.queries["SET_FEEDBACK_CRITERIA_QUERY1"], (self.grp_id,))
        _menu_id = response[0]
        cr_id_list = list()

        for criteria in criterias_selected:
            response = db.get_item(config.queries["SET_FEEDBACK_CRITERIA_QUERY2"], (criteria,))
            _cr_id = response[0]
            cr_id_list.append(_cr_id)

        data_list = [(_menu_id, cr_id) for cr_id in cr_id_list]
        db.add_items(config.queries["SET_FEEDBACK_CRITERIA_QUERY3"], data_list)

    @staticmethod
    def get_fdb_criteria():
        db = Database()
        response = db.get_items(config.queries["GET_FDB_CRITERIAS"])
        criteria = [line[0] for line in response]
        return criteria

    @staticmethod
    def add_new_criteria(new_criteria):
        db = Database()
        data_tuple = [(criteria,) for criteria in new_criteria]
        db.add_items(config.queries["UPDATE_CRITERIA"], data_tuple)

    @staticmethod
    def display_criteria(data):
        t = PrettyTable(["S No.", "Criteria"])
        t.title = f"Criteria List"
        for index, item in enumerate(data, start=1):
            t.add_row([f"{index}", f"{item}"])
        print(t)
