import json
from unittest import TestCase, mock

from src.controllers.user import User
from src.utils import config


class TestOrder(TestCase):
    def setUp(self):
        self.obj = User("dummy")
        with open(r"C:\Users\umani\Desktop\clone\data.json", "r") as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    @mock.patch("src.models.database.Database.get_item")
    def test_check_order(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.check_order()
        self.assertEqual(response, [])

    @mock.patch("src.models.database.Database.add_item")
    def test_store_order(self, mocked_add_items):
        mocked_add_items.return_value = []
        response = self.obj.store_order(1,1,1)
        self.assertEqual(response, None)
