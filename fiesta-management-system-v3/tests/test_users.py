import json
from unittest import mock
from unittest import TestCase

from src.controllers.user import User
from src.helpers.exceptions import DbException, NoSuchUserError
from src.utils import config


class TestUsers(TestCase):
    def setUp(self):
        self.obj = User("umani")
        with open("data.json", "r") as file:
            data = json.load(file)
            config.queries = data["queries"]

    @mock.patch("src.controllers.user.db")
    def test_get_details_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [
            (1, "umani", "admin", 1),
        ]

        response = self.obj.get_details()
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, True)

    @mock.patch("src.controllers.user.db")
    def test_get_details_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        with self.assertRaises(DbException):
            self.obj.get_details()
            mocked_db_object.get_items.assert_called_once()

    @mock.patch("src.controllers.user.db")
    def test_get_users_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [(1, 137, 0), (2, 233.0)]

        response = self.obj.get_users(1)
        self.assertEqual(
            response,
            [
                {"user_id": 1, "balance": 137.0},
                {"user_id": 2, "balance": 233.0},
            ],
        )
        mocked_db_object.get_items.assert_called_once()

    @mock.patch("src.controllers.user.db")
    def test_get_users_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        with self.assertRaises(NoSuchUserError):
            self.obj.get_users(1)
            mocked_db_object.get_items.assert_called_once()
