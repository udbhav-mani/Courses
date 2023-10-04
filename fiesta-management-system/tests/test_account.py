import json
from unittest import mock
from unittest import TestCase

from src.controllers.account import Account
from src.utils import config


class TestAccount(TestCase):
    def setUp(self):
        self.obj = Account()
        with open(
            r"C:\Users\umani\Desktop\Courses\fiesta-management-system\data.json", "r"
        ) as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    @mock.patch("src.models.database.Database.get_item")
    def test_view_balance(self, mocked_get_item):
        mocked_get_item.return_value = (137,)
        response = self.obj.view_balance(user_id=1)

        self.assertEqual(response, 137)

    @mock.patch("src.models.database.Database.update_item")
    def test_update_balance(self, mocked_get_item):
        mocked_get_item.return_value = []
        response = self.obj.update_balance(1, 1)

        self.assertEqual(response, None)

    @mock.patch("src.models.database.Database.update_item")
    def test_update_balance_userIdNone(self, mocked_get_item):
        mocked_get_item.return_value = []
        response = self.obj.update_balance(1, user_id=1)

        self.assertEqual(response, None)
