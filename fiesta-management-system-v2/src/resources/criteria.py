from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import (
    jwt_required,
    get_jwt,
)
from flask import request, abort

from src.controllers.criteria import Criteria
from src.helpers.validators import Validators
from src.schemas import CriteriaSchema
from src.helpers.exceptions import error


blp = Blueprint("Criteria", "Criteria", description="Operations on Criterias")


@blp.route("/criterias")
class GetCriteria(MethodView):
    @jwt_required()
    def get(self):
        role = get_jwt().get("role")
        if role not in ["admin", "emp"]:
            return error(code=403, message="You are not authorised to do this.")
        criteria = Criteria()
        response = criteria.get_fdb_criteria()
        return response

    @jwt_required()
    def post(self):
        role = get_jwt().get("role")
        if role not in ["admin"]:
            return error(code=403, message="You are not authorised to do this.")

        data = request.get_json()
        validator = Validators.validate_request(CriteriaSchema, data)
        if validator:
            return error(code=400, message=validator.split("\n")[0])

        criteria = Criteria()
        criteria.add_new_criteria(data["criteria"])
        return dict(message="Criteria added successfully", status="success"), 200
