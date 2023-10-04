import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import json

from flask import Flask, jsonify
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

with open(
    r"C:\Users\umani\Desktop\Courses\fiesta-management-system-v2\data.json", "r"
) as file:
    data = json.load(file)
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

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "error": {"code": 400, "message": "The token has expired."},
                    "status": "failure",
                }
            ),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {
                    "error": {"code": 400, "message": "Signature verification failed."},
                    "status": "failure",
                }
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "error": {
                        "code": 400,
                        "message": "Request does not contain an access token.",
                    },
                    "status": "failure",
                }
            ),
            401,
        )

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
