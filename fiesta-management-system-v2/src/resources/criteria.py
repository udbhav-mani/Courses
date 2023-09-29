from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import (
    jwt_required, get_jwt,
)
from flask import request, abort

from src.controllers.criteria import Criteria
from src.helpers.validators import Validators
from src.schemas import CriteriaSchema

blp = Blueprint("Criteria", "Criteria", description="Operations on Criterias")


@blp.route("/criterias")
class GetCriteria(MethodView):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role not in ["admin", "emp"]:
            abort(403, message="You are not authorised to do this.")
        criteria = Criteria()
        response = criteria.get_fdb_criteria()
        return response

    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role not in ["admin"]:
            abort(403, message="You are not authorised to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(CriteriaSchema, data)
        if is_validated is not None:
            return {
                "error": {"code": 400, "message": is_validated.split("\n")[0]},
                "status": "failure",
            }, 400

        criteria = Criteria()
        criteria.add_new_criteria(data["criteria"])
        return dict(message="success"), 200
