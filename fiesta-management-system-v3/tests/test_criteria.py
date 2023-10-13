import json
from unittest import mock
from unittest import TestCase

from src.controllers.criteria import Criteria
from src.helpers.exceptions import DbException
from src.utils import config


class TestCriteria(TestCase):
    def setUp(self):
        self.obj = Criteria()


    @mock.patch("src.controllers.criteria.db")
    def test_set_fdb_criteria_success(self, mocked_db_object):
        mocked_db_object.get_item.return_value = (1, 2, 3)
        mocked_db_object.add_items.return_value = 22

        response = self.obj.set_fdb_criteria({"criteria": ["taste", "color"]}, 1)
        self.assertEqual(response, 22)

    @mock.patch("src.controllers.criteria.db")
    def test_set_fdb_criteria_failure(self, mocked_db_object):
        mocked_db_object.get_item.return_value = (1, 2, 3)
        mocked_db_object.add_items.return_value = None

        with self.assertRaises(DbException):
            self.obj.set_fdb_criteria({"criteria": ["taste", "color"]}, -1)

    @mock.patch("src.controllers.criteria.db")
    def test_get_fdb_criteria_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [(1, "taste"), (2, "color")]

        response = self.obj.get_fdb_criteria()
        self.assertEqual(
            response, [{"id": 1, "criteria": "taste"}, {"id": 2, "criteria": "color"}]
        )

    @mock.patch("src.controllers.criteria.db")
    def test_get_fdb_criteria_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        with self.assertRaises(DbException):
            self.obj.get_fdb_criteria()

    @mock.patch("src.controllers.criteria.db")
    def test_add_new_criteria_success(self, mocked_db_object):
        mocked_db_object.add_items.return_value = 3

        response = self.obj.add_new_criteria(["taste", "creamy"])
        self.assertEqual(response, 3)

    @mock.patch("src.controllers.criteria.db")
    def test_add_new_criteria_failure(self, mocked_db_object):
        mocked_db_object.add_items.return_value = None

        with self.assertRaises(DbException):
            self.obj.add_new_criteria([1, "creamy"])
