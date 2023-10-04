from flask_smorest import Blueprint, abort
from flask.views import MethodView, request
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
)

from src.controllers.criteria import Criteria
from src.controllers.feedback import Feedback
from src.controllers.menu import Menu
from src.controllers.user import User
from src.helpers.validators import Validators
from src.schemas import CriteriaSchema, PlainFeedbackSchema
from src.helpers.exceptions import error


blp = Blueprint("Feedback", "Feedback", description="Operations on Feedback")


@blp.route("/feedback/criterias")
class FeedbackCriterias(MethodView):
    @jwt_required()
    def get(self):
        grp_id = get_jwt().get("grp_id")
        response = User.get_menu_fdb_criterias(grp_id)
        if response is None:
            return error(
                code=400, message="No criterias have been decided for current menu."
            )

        return response

    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role not in ["admin"]:
            return error(code=403, message="You are not authorized to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(CriteriaSchema, data)
        if is_validated is not None:
            return error(code=400, message=is_validated.split("\n")[0])

        criteria = Criteria()
        criteria.set_fdb_criteria(
            criterias_selected=data, grp_id=get_jwt().get("grp_id")
        )
        return dict(criterias=data, grp_id=get_jwt().get("grp_id"))


@blp.route("/feedback")
class FDB(MethodView):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role not in ["admin", "emp"]:
            return error(code=403, message="You are not authorized to do this.")

        criteria = request.args.get("criteria")
        feedback = Feedback()
        response = feedback.view_all_feedbacks(get_jwt().get("grp_id"))
        feedback = Feedback()
        if criteria is not None:
            filtered_response = []
            for item in response:
                if item.get("criteria") == criteria:
                    filtered_response.append(item)
            return filtered_response
        return response

    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role not in ["admin", "emp"]:
            return error(code=403, message="You are not authorized to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(PlainFeedbackSchema, data)
        if is_validated is not None:
            return error(code=400, message=is_validated.split("\n")[0])

        user_id = get_jwt().get("user_id")
        grp_id = get_jwt().get("grp_id")
        menu_id = Menu.get_menu_from_group(grp_id)
        var = [
            (user_id, item["cr_id"], menu_id, int(item["feedback"]), item["comments"])
            for item in data
        ]
        User.add_feedback(var)
        return dict(message="success")
