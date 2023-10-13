import json
from unittest import mock
from unittest import TestCase

from src.controllers.account import Account
from src.helpers.exceptions import DbException, NoSuchUserError
from src.utils import config


class TestAccount(TestCase):
    def setUp(self):
        self.obj = Account()


    @mock.patch("src.controllers.account.db")
    def test_view_balance_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = (197.0, 2)

        response = self.obj.view_balance(2)
        mocked_db_object.get_item.assert_called_once()
        self.assertEqual(response, 197.0)

    @mock.patch("src.controllers.account.db")
    def test_view_balance_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = None

        with self.assertRaises(NoSuchUserError):
            self.obj.view_balance(99)
            mocked_db_object.get_item.assert_called_once()

    @mock.patch("src.controllers.account.db")
    def test_update_balance_success(self, mocked_db_object):
        mocked_db_object.update_item.return_value = 1

        response = self.obj.update_balance(1, 2)
        mocked_db_object.update_item.assert_called_once()
        self.assertEqual(response, 1)

    @mock.patch("src.controllers.account.db")
    def test_update_balance_failure(self, mocked_db_object):
        mocked_db_object.update_item.return_value = None

        with self.assertRaises(DbException):
            self.obj.update_balance(99, -1)
            mocked_db_object.update_item.assert_called_once()
