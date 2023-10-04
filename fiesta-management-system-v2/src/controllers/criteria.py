from src.models.database import Database
from src.utils import config


class Criteria:
    def set_fdb_criteria(self, criterias_selected, grp_id):
        db = Database()
        response = db.get_item(
            config.queries["SET_FEEDBACK_CRITERIA_QUERY1"], (grp_id,)
        )
        _menu_id = response[0]
        cr_id_list = list()

        print(criterias_selected)

        for criteria in criterias_selected["criteria"]:
            response = db.get_item(
                config.queries["SET_FEEDBACK_CRITERIA_QUERY2"], (criteria,)
            )
            _cr_id = response[0]
            cr_id_list.append(_cr_id)

        data_list = [(_menu_id, cr_id) for cr_id in cr_id_list]
        db.add_items(config.queries["SET_FEEDBACK_CRITERIA_QUERY3"], data_list)

    @staticmethod
    def get_fdb_criteria():
        db = Database()
        # print(config.queries["GET_FDB_CRITERIAS"])
        response = db.get_items(config.queries["GET_FDB_CRITERIAS"], data=None)
        criteria = [dict(id=line[0], criteria=line[1]) for line in response]
        return criteria

    @staticmethod
    def add_new_criteria(new_criteria):
        db = Database()
        data_tuple = [(criteria,) for criteria in new_criteria]
        db.add_items(config.queries["UPDATE_CRITERIA"], data_tuple)
