from src.models.database import Database


class Criteria:
    def set_fdb_criteria(self, criterias_selected, grp_id):
        db = Database()
        SET_FEEDBACK_CRITERIA_QUERY1 = 'select menu_id from `groups` where id = %s'
        SET_FEEDBACK_CRITERIA_QUERY2 = 'select id from `fdb_criterias` where criteria = %s'
        SET_FEEDBACK_CRITERIA_QUERY3 = 'insert into `menu_fdb_criterias` (menu_id, cr_id) values(%s,%s)'

        response = db.get_item(SET_FEEDBACK_CRITERIA_QUERY1, (grp_id,))
        _menu_id = response[0]
        cr_id_list = list()

        print(criterias_selected)

        for criteria in criterias_selected["criteria"]:
            response = db.get_item(SET_FEEDBACK_CRITERIA_QUERY2, (criteria,))
            _cr_id = response[0]
            # print(_cr_id)
            cr_id_list.append(_cr_id)

        data_list = [(_menu_id, cr_id) for cr_id in cr_id_list]
        db.add_items(SET_FEEDBACK_CRITERIA_QUERY3, data_list)

    @staticmethod
    def get_fdb_criteria():
        db = Database()
        GET_FDB_CRITERIAS = "SELECT id, criteria from fdb_criterias"
        response = db.get_items(GET_FDB_CRITERIAS, data=None)
        criteria = [dict(id=line[0], criteria= line[1]) for line in response]
        return criteria

    @staticmethod
    def add_new_criteria(new_criteria):
        db = Database()
        data_tuple = [(criteria,) for criteria in new_criteria]
        UPDATE_CRITERIA = "insert into fdb_criterias(criteria) values(%s)"
        db.add_items(UPDATE_CRITERIA, data_tuple)



if __name__ == "__main__":
    criteria = Criteria()
    criteria.set_fdb_criteria(["taste", "quality"], 1)