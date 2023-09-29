from flask_smorest import Blueprint, abort
from flask.views import MethodView, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)

from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.exceptions import NoSuchUserError
from src.schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/login")
class UserLogin(MethodView):
    def post(self):
        user_data = request.get_json()
        instance = Login()
        try:
            is_authenticated = instance.authenticate_credentials(user_name=user_data["username"],
                                                                 password=user_data["password"])
            if isinstance(is_authenticated,str):
                abort(404, message="No such user found")
        except NoSuchUserError:
            abort(404, message="No such user found")
        else:
            if is_authenticated:
                access_token = create_access_token(identity=user_data["username"])
                return {"access_token": access_token}, 200

            else:
                abort(401, message="Invalid credentials.")


@blp.route("/users")
class UserLogin(MethodView):
    @jwt_required()
    def get(self):
        grp_id = request.args.get("grp_id")
        user_id = request.args.get("user_id")
        user = User()
        response = user.get_users(grp_id=grp_id)
        if user_id is not None:
            for item in response:
                if item.get("user_id") == int(user_id):
                    return item
            else:
                abort(404, message="user_id not found")
        else:
            return response

