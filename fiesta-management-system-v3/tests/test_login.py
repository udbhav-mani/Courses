import json
from unittest import TestCase, mock

from src.controllers.login import Login
from src.helpers.exceptions import LoginError
from src.utils import config


class TestLogin(TestCase):
    def setUp(self):
        self.obj = Login()
        with open("data.json", "r") as file:
            data = json.load(file)
            config.queries = data["queries"]

    def test_authenticate_credentials_success(self):
        response = self.obj.authenticate_credentials("umani", "Udbhavpass1!")
        self.assertEqual(response, None)

    def test_authenticate_credentials_failure(self):
        with self.assertRaises(LoginError):
            self.obj.authenticate_credentials("umani", "wrong pass!")
