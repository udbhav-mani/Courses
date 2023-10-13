import json
from unittest import mock
from unittest import TestCase

from src.controllers.orders import Orders
from src.helpers.exceptions import DbException
from src.utils import config


class TestOrders(TestCase):
    def setUp(self):
        self.obj = Orders()
        with open("data.json", "r") as file:
            data = json.load(file)
            config.queries = data["queries"]

    @mock.patch("src.controllers.orders.db")
    def test_check_order_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [
            (11, 2, 137.0, "2020-11-29T18:25:43.511Z"),
            (12, 3, 137.0, "2020-11-30T18:25:43.511Z"),
        ]

        response = self.obj.check_order(2)
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(
            response,
            [
                {"order_id": 11, "user_id": 2, "amount": 137.0, "date": "2020-11-29"},
                {"order_id": 12, "user_id": 3, "amount": 137.0, "date": "2020-11-30"},
            ],
        )

    @mock.patch("src.controllers.orders.db")
    def test_check_order_with_date_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [
            (11, 2, 137.0, "2020-11-29T18:25:43.511Z"),
            (12, 3, 137.0, "2020-11-30T18:25:43.511Z"),
        ]

        response = self.obj.check_order(2, "2020-11-29")
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(
            response,
            [{"order_id": 11, "user_id": 2, "amount": 137.0, "date": "2020-11-29"}],
        )

    @mock.patch("src.controllers.orders.db")
    def test_check_order_with_date_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        response = self.obj.check_order(2, "2020-11-29")
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, [])

    @mock.patch("src.controllers.orders.db")
    def test_check_order_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        response = self.obj.check_order(2)
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(response, [])

    @mock.patch("src.controllers.orders.db")
    def test_store_order_success(self, mocked_db_object):
        mocked_db_object.add_item.return_value = 23

        response = self.obj.store_order(2, 137.0, "umani")
        mocked_db_object.add_item.assert_called_once()
        self.assertEqual(response, 23)

    @mock.patch("src.controllers.orders.db")
    def test_store_order_failure(self, mocked_db_object):
        mocked_db_object.add_item.return_value = None

        with self.assertRaises(DbException):
            self.obj.store_order(-2, 137.0, "umani")
            mocked_db_object.add_item.assert_called_once()
