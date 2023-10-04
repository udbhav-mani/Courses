from datetime import datetime

from flask_smorest import Blueprint, abort
from flask.views import MethodView, request
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
)

from src.controllers.account import Account
from src.controllers.menu import Menu
from src.helpers.validators import Validators
from src.schemas import MenuSchema, UpdateSchema, UpdateItemSchema
from src.helpers.exceptions import error

blp = Blueprint("Menu", "Menu", description="Operations on menu")


@blp.route("/menu")
class GetMenu(MethodView):
    @jwt_required()
    def get(self):
        grp_id = get_jwt().get("grp_id")
        menu = Menu()
        status = request.args.get("status")
        if status not in [
            "pending",
            "published",
            "not published",
            "rejected",
            "discarded",
        ]:
            return error(
                code=400,
                message="Invalid status, must be from pending, published, not published, rejected, "
                "discarded",
            )
        if status == "published":
            response = menu.view_accepted_menu(grp_id=grp_id)
        else:
            response = menu.get_menu_by_status(grp_id=grp_id, status=status)

        if len(response) == 0:
            return error(code=400, message="No such menu found.")
        else:
            date = response[0][1]
            items = [item[0] for item in response]
            return dict(menu_id=response[0][2], date=date, items=items)

    @jwt_required()
    def post(self):
        grp_id = get_jwt().get("grp_id")
        role = get_jwt().get("role")
        if role not in ["admin"]:
            return error(code=403, message="You are not authorised to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(MenuSchema, data)
        if is_validated is not None:
            return error(code=400, message=is_validated.split("\n")[0])

        menu = Menu()
        items = data["items"]
        name = get_jwt().get("sub")
        date = data["date"]
        datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        response = menu.propose_menu(items, datetime_object, name, grp_id)
        return dict(message=response)

    @jwt_required()
    def put(self):
        grp_id = get_jwt().get("grp_id")
        data = request.get_json()
        menu = Menu()
        role = get_jwt().get("role")
        if role not in ["admin", "f_emp"]:
            return error(code=403, message="You are not authorised to do this.")

        is_validated = Validators.validate_request(UpdateSchema, data)
        if is_validated is not None:
            return error(code=400, message=is_validated.split("\n")[0])

        menu_id = data["menu_id"]
        status = data["status"]

        if status not in [
            "pending",
            "published",
            "not published",
            "rejected",
            "discarded",
        ]:
            return error(
                code=400,
                message="Invalid status, must be from pending, published, not published, rejected, "
                "discarded",
            )
        else:
            if status == "published":
                response = menu.get_menu_by_status(
                    grp_id=grp_id, status="not published"
                )
                date = response[0][1]
                menu.publish_menu(menu_id=menu_id, grp_id=grp_id, menu_date=date)
                account = Account()
                account.update_balance(amount=137, grp_id=grp_id)
                return dict(message="success")

            elif status == "rejected":
                comments = data["comments"]
                username = get_jwt().get("sub")
                response = menu.reject_menu(
                    menu_id=menu_id, comments=comments, username=username
                )
                return dict(message=response)
            else:
                response = menu.update_menu_status(status, menu_id)
                return dict(message=response)


@blp.route("/menu/<int:menu_id>")
class GetMenu(MethodView):
    @jwt_required()
    def patch(self, menu_id):
        menu = Menu()
        role = get_jwt().get("role")
        if role not in ["admin", "f_emp"]:
            abort(403, message="You are not authorized to do this.")

        data = request.get_json()
        is_validated = Validators.validate_request(UpdateItemSchema, data)
        if is_validated is not None:
            return {
                "error": {"code": 400, "message": is_validated.split("\n")[0]},
                "status": "failure",
            }, 400

        menu.update_menu(
            menu_id=menu_id, old_item=data["old_item"], new_item=data["new_item"]
        )
        return dict(message="success", new_item=data["new_item"], menu_id=menu_id)
