from src.models.database import Database


class Feedback:
    @staticmethod
    def view_all_feedbacks(grp_id):
        db = Database()
        VIEW_FEEDBACK = (
            "select c.criteria, f.feedback, f.comments from `groups` as g inner join menu_fdb as f on "
            "f.menu_id = g.menu_id inner join fdb_criterias as c on f.cr_id = c.id where g.id = %s;"
        )

        response = db.get_items(VIEW_FEEDBACK, (grp_id,))
        return [
            dict(criteria=tup[0], feedback=tup[1], comments=tup[2]) for tup in response
        ]

    @staticmethod
    def get_menu_fdb_criterias(grp_id):
        db = Database()
        GET_MENU_FDB_CRITERIAS = (
            "select distinct g.menu_id,r.id,r.criteria from `groups` as g inner join "
            "menu_fdb_criterias as f on g.menu_id = f.menu_id inner join fdb_criterias as r on "
            "f.cr_id = r.id where g.id = %s"
        )

        response = db.get_items(GET_MENU_FDB_CRITERIAS, (grp_id,))
        if len(response) > 0:
            criterias = [{"cr_id": tup[1], "criteria": tup[2]} for tup in response]
            return criterias

        return None

    @staticmethod
    def add_feedback(feedback):
        db = Database()
        ADD_FEEDBACK = "INSERT into `menu_fdb`(user_id, cr_id, menu_id, feedback, comments) values(%s,%s,%s,%s,%s)"

        db.add_items(ADD_FEEDBACK, feedback)
