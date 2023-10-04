from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
)

from src.helpers.exceptions import error

from flask import request
from src.controllers.user import User
from src.helpers.validators import Validators

from src.schemas import OrderSchema

blp = Blueprint("Orders", "Orders", description="Operations on orders")


@blp.route("/orders")
class PlaceOrder(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()
        validator = Validators.validate_request(OrderSchema, data)
        if validator:
            return error(code=400, message=validator.split("\n")[0])

        user = User()
        user.update_balance(amount=-1 * data["amount"], user_id=data["user_id"])
        order_id = User.store_order(
            amount=data["amount"],
            user_id=data["user_id"],
            created_by=get_jwt().get("sub"),
        )
        return {
            "message": "success",
            "amount": data["amount"],
            "order_id": order_id,
        }, 201


@blp.route("/orders/<int:user_id>")
class GetOrder(MethodView):
    @jwt_required()
    def get(self, user_id):
        user = User()
        date = request.args.get("date")
        if date is None:
            data = user.check_order(user_id=user_id)
            return data
        else:
            data = user.check_order(user_id=user_id, date=date)
            return data
