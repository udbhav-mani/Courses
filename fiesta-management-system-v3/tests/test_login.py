import json
from unittest import TestCase, mock

from src.controllers.login import Login
from src.utils import config


class TestLogin(TestCase):
    def setUp(self):
        self.obj = Login()
        with open(r"C:\Users\umani\Desktop\clone\data.json", "r") as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]


    def test_authenticate_credentials(self):
        response = self.obj.authenticate_credentials("umani", "Udbhavpass1!")
        self.assertEqual(response, True)

