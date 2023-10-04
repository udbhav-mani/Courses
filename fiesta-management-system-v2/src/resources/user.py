from src.helpers.validators import Validators
from flask_smorest import Blueprint, abort
from flask.views import MethodView, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.exceptions import NoSuchUserError, error


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/login")
class UserLogin(MethodView):
    def post(self):
        user_data = request.get_json()
        instance = Login()
        try:
            is_authenticated = instance.authenticate_credentials(
                user_name=user_data.get("username"), password=user_data.get("password")
            )
            if isinstance(is_authenticated, str):
                return error(code=404, message="No such user found")
        except NoSuchUserError:
            return error(code=404, message="No such user found")
        else:
            if is_authenticated:
                access_token = create_access_token(identity=user_data["username"])
                return {"access_token": access_token}, 200
            else:
                return error(code=401, message="Invalid credentials.")


@blp.route("/users")
class UserLogin(MethodView):
    @jwt_required()
    def get(self):
        grp_id = get_jwt().get("grp_id")
        user_id = request.args.get("user_id")
        if not Validators.validate_id(user_id):
            return error(code=400, message="Please give appropriate user_id")

        user = User()
        response = user.get_users(grp_id=grp_id)
        if user_id is not None:
            for item in response:
                if item.get("user_id") == int(user_id):
                    return [item]
            else:
                return error(code=404, message="user_id not found")
        else:
            return response
