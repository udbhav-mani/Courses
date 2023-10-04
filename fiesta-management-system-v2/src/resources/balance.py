from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
)
from flask import request
from src.helpers.exceptions import error

from controllers.account import Account
from schemas import UpdateUserBalanceSchema
from schemas import UpdateGrpBalanceSchema

from src.helpers.validators import Validators

blp = Blueprint("Balance", "balance", description="Operations on balance")


@blp.route("/balance")
class UserBalance(MethodView):
    @jwt_required()
    def get(self):
        user_id = request.args.get("user_id")
        if not Validators.validate_id(user_id):
            return error(code=400, message="Please give appropriate user_id")
        account = Account()
        balance = account.view_balance(user_id=user_id)
        if balance:
            return {
                "id": user_id,
                "balance": balance,
                "grp_id": get_jwt().get("grp_id"),
            }, 200
        else:
            return error(code=404, message="No such user found.")


@blp.route("/balance/user")
class UpdateUserBalance(MethodView):
    @jwt_required()
    def put(self):
        role = get_jwt().get("role")
        if role not in ["admin", "f_emp"]:
            return error(code=403, message="You are not authorised to do this.")

        data = request.get_json()
        validator = Validators.validate_request(UpdateUserBalanceSchema, data)
        if validator:
            return error(code=400, message=validator.split("\n")[0])

        account = Account()
        account.update_balance(amount=data["amount"], user_id=data["user_id"])
        return {
            "message": "success",
            "amount": data["amount"],
            "user_id": data["user_id"],
        }, 200


@blp.route("/balance/grp")
class UpdateGroupBalance(MethodView):
    @jwt_required()
    def put(self):
        role = get_jwt().get("role")
        if role not in ["admin"]:
            return error(code=403, message="You are not authorised to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(UpdateGrpBalanceSchema, data)
        if is_validated is not None:
            return error(code=400, message=is_validated.split("\n")[0])

        account = Account()
        account.update_balance(amount=data["amount"], grp_id=data["grp_id"])
        return {
            "message": "success",
            "amount": data["amount"],
            "grp_id": data["grp_id"],
        }, 200
