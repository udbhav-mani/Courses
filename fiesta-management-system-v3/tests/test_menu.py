import datetime
import json
from unittest import TestCase, mock

from src.controllers.user import User
from src.helpers.exceptions import DbException, NoMenuFoundError
from src.utils import config


class TestMenu(TestCase):
    def setUp(self):
        self.obj = User("dummy")
        with open("data.json", "r") as file:
            data = json.load(file)
            config.queries = data["queries"]

    @mock.patch("src.controllers.menu.db")
    def test_view_accepted_menu_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [1, 2, 3]

        response = self.obj.view_accepted_menu(1)
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, [1, 2, 3])

    @mock.patch("src.controllers.menu.db")
    def test_view_accepted_menu_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        with self.assertRaises(NoMenuFoundError):
            self.obj.view_accepted_menu(99)
            mocked_db_object.get_items.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_get_menu_from_group_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = [29]

        response = self.obj.get_menu_from_group(1)
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, 29)

    @mock.patch("src.controllers.menu.db")
    def test_get_menu_from_group_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = None

        with self.assertRaises(NoMenuFoundError):
            self.obj.get_menu_from_group(7)
            mocked_db_object.get_item.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_propose_menu_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 1
        mocked_db_object.add_items.return_value = 1

        response = self.obj.propose_menu(
            ["rajma", "chawal", "roti", "dahi", "papad"],
            "2020-11-29 18:25:43.511000",
            "umani",
            1,
        )
        mocked_db_object.add_item.assert_called_once()
        mocked_db_object.add_items.assert_called_once()
        self.assertEqual(response, True)

    @mock.patch("src.controllers.menu.db")
    def test_propose_menu_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = None
        mocked_db_object.add_items.return_value = 1

        with self.assertRaises(DbException):
            self.obj.propose_menu(
                ["rajma", "chawal", "roti", "dahi", "papad"],
                "2020-11-29 18:25:43.511000",
                "umani",
                99,
            )
            mocked_db_object.add_item.assert_called_once()
            mocked_db_object.add_items.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_update_menu_status_success(self, mocked_db_object):
        mocked_db_object.update_item.return_value = 1
        response = self.obj.update_menu_status("pending", 22)
        mocked_db_object.update_item.assert_called_once()
        self.assertEqual(response, True)

    @mock.patch("src.controllers.menu.db")
    def test_update_menu_status_failure(self, mocked_db_object):
        mocked_db_object.update_item.return_value = None

        with self.assertRaises(DbException):
            self.obj.update_menu_status("invalid_string", 22)
            mocked_db_object.update_item.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_update_menu_success(self, mocked_db_object):
        mocked_db_object.update_item.return_value = 1
        self.obj.update_menu_status = mock.MagicMock()
        self.obj.update_menu_status.return_value = True

        response = self.obj.update_menu(22, "rajma", "chole")
        mocked_db_object.update_item.assert_called_once()
        self.assertEqual(response, 1)

    @mock.patch("src.controllers.menu.db")
    def test_update_menu_failure(self, mocked_db_object):
        mocked_db_object.update_item.return_value = None
        self.obj.update_menu_status = mock.MagicMock()
        self.obj.update_menu_status.return_value = True

        with self.assertRaises(NoMenuFoundError):
            self.obj.update_menu(99, "rajma", "chole")
            mocked_db_object.update_item.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_publish_menu_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 1
        mocked_db_object.update_item.return_value = 1

        response = self.obj.publish_menu(1, datetime.date(2023, 9, 25), 1)
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(mocked_db_object.update_item.call_count, 2)
        self.assertEqual(response, 1)

    @mock.patch("src.controllers.menu.db")
    def test_publish_menu_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 1
        mocked_db_object.update_item.return_value = None

        with self.assertRaises(DbException):
            self.obj.publish_menu(1, "2023, 9, 25", 1)
            mocked_db_object.add_item.assert_called_once()
            self.assertEqual(mocked_db_object.update_item.call_count, 2)

    @mock.patch("src.controllers.menu.db")
    def test_get_menu_by_status_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [
            29,
            ("rajma", "chawal", "dahi"),
            datetime.date(2023, 9, 25),
        ]

        response = self.obj.get_menu_by_status(1, "pending")
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(
            response,
            [
                29,
                ("rajma", "chawal", "dahi"),
                datetime.date(2023, 9, 25),
            ],
        )

    @mock.patch("src.controllers.menu.db")
    def test_get_menu_by_status_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = None

        with self.assertRaises(NoMenuFoundError):
            self.obj.get_menu_by_status(1, "invalid_string")
            mocked_db_object.get_items.assert_called_once()

    @mock.patch("src.controllers.menu.db")
    def test_reject_menu_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 37
        self.obj.update_menu_status = mock.MagicMock()
        self.obj.update_menu_status.return_value = True

        response = self.obj.reject_menu(29, "good food", "umani")
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, 37)

    @mock.patch("src.controllers.menu.db")
    def test_reject_menu_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = None
        self.obj.update_menu_status = mock.MagicMock()
        self.obj.update_menu_status.return_value = True

        with self.assertRaises(NoMenuFoundError):
            self.obj.reject_menu(99, "good food", "umani")
            mocked_db_object.add_item.assert_called_once()
