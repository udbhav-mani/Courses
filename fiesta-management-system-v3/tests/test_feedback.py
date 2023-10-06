import json
from unittest import TestCase, mock

from src.controllers.user import User
from src.utils import config


class TestFeedback(TestCase):
    def setUp(self):
        self.obj = User("dummy")
        with open(r"C:\Users\umani\Desktop\clone\data.json", "r") as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    @mock.patch("src.models.database.Database.get_items")
    def test_view_all_feedbacks(self, mocked_get_item):
        mocked_get_item.return_value = [("taste", 4, "good")]
        response = self.obj.view_all_feedbacks()
        fdb = [("taste", 4, "good")]
        self.assertEqual(response, [("taste", 4, "good")])

    @mock.patch("src.models.database.Database.get_items")
    def test_get_menu_fdb_criterias_zero(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.get_menu_fdb_criterias()
        self.assertEqual(response, None)

    @mock.patch("src.models.database.Database.get_items")
    def test_get_menu_fdb_criterias(self, mocked_get_items):
        mocked_get_items.return_value = [(1, 1, "taste",), (1, 2, "quality",)]
        response = self.obj.get_menu_fdb_criterias()
        fdb = [
            {
                "menu_id": 1,
                "cr_id": 1,
                "criteria": "taste"
            },
            {
                "menu_id": 1,
                "cr_id": 2,
                "criteria": "quality"
            }
        ]

        self.assertEqual(response, fdb)

    @mock.patch("src.models.database.Database.get_item")
    def test_check_user_feedback_zero(self, mocked_get_item):
        mocked_get_item.return_value = None
        response = self.obj.check_user_feedback()
        self.assertEqual(response, False)

    @mock.patch("src.models.database.Database.get_item")
    def test_check_user_feedback(self, mocked_get_item):
        mocked_get_item.return_value = []
        response = self.obj.check_user_feedback()
        self.assertEqual(response, True)

