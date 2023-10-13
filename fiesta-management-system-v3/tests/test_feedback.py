import json
from unittest import mock
from unittest import TestCase

from src.controllers.feedback import Feedback
from src.helpers.exceptions import DbException, NotFoundException
from src.utils import config


class TestFeedback(TestCase):
    def setUp(self):
        self.obj = Feedback()
        with open("data.json", "r") as file:
            data = json.load(file)
            config.queries = data["queries"]

    @mock.patch("src.controllers.feedback.db")
    def test_get_menu_fdb_criterias_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [(32, 1, "taste"), (32, 2, "color")]

        response = self.obj.get_menu_fdb_criterias(1)
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(
            response,
            [{"cr_id": 1, "criteria": "taste"}, {"cr_id": 2, "criteria": "color"}],
        )

    @mock.patch("src.controllers.feedback.db")
    def test_get_menu_fdb_criteria_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = []

        with self.assertRaises(NotFoundException):
            self.obj.get_menu_fdb_criterias(1)
            mocked_db_object.get_items.assert_called_once()

    @mock.patch("src.controllers.feedback.db")
    def test_add_feedback_success(self, mocked_db_object):
        mocked_db_object.add_items.return_value = 3

        response = self.obj.add_feedback((1, 3, 32, 4.5, "good_taste"))
        mocked_db_object.add_items.assert_called_once()
        self.assertEqual(response, 3)

    @mock.patch("src.controllers.feedback.db")
    def test_add_feedback_failure(self, mocked_db_object):
        mocked_db_object.add_items.return_value = None

        with self.assertRaises(DbException):
            self.obj.add_feedback((1, 3, 32, 4.5, "good_taste"))
            mocked_db_object.add_items.assert_called_once()

    @mock.patch("src.controllers.feedback.db")
    def test_view_all_feedbacks_success(self, mocked_db_object):
        mocked_db_object.get_items.return_value = [("taste", 3.5, "good taste")]

        response = self.obj.view_all_feedbacks(32)
        mocked_db_object.get_items.assert_called_once()
        self.assertEqual(
            response, [{"criteria": "taste", "feedback": 3.5, "comments": "good taste"}]
        )

    @mock.patch("src.controllers.feedback.db")
    def test_view_all_feedbacks_failure(self, mocked_db_object):
        mocked_db_object.get_items.return_value = None

        with self.assertRaises(DbException):
            self.obj.view_all_feedbacks(32)
            mocked_db_object.get_items.assert_called_once()
