import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import json

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager


from src.resources.user import blp as UserBlueprint
from src.resources.balance import blp as BalanceBlueprint
from src.resources.orders import blp as OrdersBlueprint
from src.resources.menu import blp as MenuBlueprint
from src.resources.criteria import blp as CriteriaBlueprint
from src.resources.feedback import blp as FeedbackBlueprint
from src.controllers.user import User
from utils import config

with open(r"C:\Users\umani\Desktop\clone\data.json", "r") as file:
    print("File imported")
    data = json.load(file)
    config.prompts = data["menu_choices"]
    config.queries = data["queries"]


def create_app():
    app = Flask(__name__)


    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Fiesta Management API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "jose"
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        user = User(user_name=identity)
        user.get_details()

        user_data = {
            "user_id": user.user_id,
            "grp_id": user.grp_id,
            "role": user.role,
        }
        return user_data

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(BalanceBlueprint)
    api.register_blueprint(OrdersBlueprint)
    api.register_blueprint(MenuBlueprint)
    api.register_blueprint(CriteriaBlueprint)
    api.register_blueprint(FeedbackBlueprint)

    return app
