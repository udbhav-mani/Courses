import json
from unittest import TestCase, mock

from src.controllers.user import User
from src.utils import config


class TestCriteria(TestCase):
    def setUp(self):
        self.obj = User("dummy")
        with open(
            r"C:\Users\umani\Desktop\Courses\fiesta-management-system\data.json", "r"
        ) as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    @mock.patch("src.models.database.Database.get_items")
    def test_get_fdb_criteria(self, mocked_get_items):
        mocked_get_items.return_value = [("taste",)]
        response = self.obj.get_fdb_criteria()
        self.assertEqual(response, ["taste"])

    @mock.patch("src.models.database.Database.add_items")
    def test_add_new_criteria(self, mocked_add_items):
        mocked_add_items.return_value = [("taste",)]
        response = self.obj.add_new_criteria([])
        self.assertEqual(response, None)

    @mock.patch("builtins.print")
    def test_display_criteria(self, mocked_add_items):
        mocked_add_items.return_value = ""
        response = self.obj.display_criteria([])
        self.assertEqual(response, None)

    @mock.patch("src.models.database.Database.get_item")
    @mock.patch("src.models.database.Database.add_items")
    def test_set_fdb_criteria(self, mocked_add_items, mocked_get_item):
        mocked_add_items.return_value = [1]
        mocked_get_item.return_value = [1]
        response = self.obj.set_fdb_criteria([])
        self.assertEqual(response, None)
