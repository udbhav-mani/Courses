import json
from unittest import TestCase, mock

from src.controllers.user import User
from src.utils import config


class TestMenu(TestCase):
    def setUp(self):
        self.obj = User("dummy")
        with open("data.json", "r") as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    @mock.patch("src.controllers.menu.Menu.display_menu")
    @mock.patch("src.models.database.Database.get_items")
    def test_view_accepted_menu(self, mocked_get_items, mocked_print):
        mocked_get_items.return_value = []
        mocked_print.return_value = []
        response = self.obj.view_accepted_menu()
        self.assertEqual(response, None)

    @mock.patch("src.models.database.Database.get_items")
    def test_get_pending_menu(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.get_pending_menu()
        self.assertEqual(response, [])

    @mock.patch("src.models.database.Database.get_items")
    def test_get_not_published_menu(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.get_not_published_menu()
        self.assertEqual(response, [])

    @mock.patch("src.models.database.Database.get_item")
    def test_check_menu_status(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.check_menu_status("")
        self.assertEqual(response, [])

    @mock.patch("src.controllers.menu.Menu.display_menu")
    @mock.patch("src.models.database.Database.get_items")
    def test_view_menu(self, mocked_get_items, mocked_print):
        mocked_get_items.return_value = []
        mocked_print.return_value = []
        response = self.obj.view_menu(1)
        self.assertEqual(response, [])

    @mock.patch("src.models.database.Database.get_item")
    def test_check_rejected_menu(self, mocked_get_items):
        mocked_get_items.return_value = []
        response = self.obj.check_rejected_menu()
        self.assertEqual(response, [])

    @mock.patch("src.models.database.Database.update_item")
    def test_update_menu(self, mocked_update_items):
        mocked_update_items.return_value = []
        response = self.obj.update_menu(1, "", "")
        self.assertEqual(response, None)
