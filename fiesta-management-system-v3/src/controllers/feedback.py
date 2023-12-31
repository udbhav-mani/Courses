"""
Provides feedback class for operations
related to feedback
"""
from src.helpers.exceptions import BadRequestException, DbException, NotFoundException
from src.models.database import db
from src.utils import config


class Feedback:
    """
    Provides methods for viewing all feedbacks, getting menu feedback criterias, and
    adding feedback.
    """

    @staticmethod
    def view_all_feedbacks(grp_id):
        """
        Retrieves all the feedbacks from a menu

        Args:
          grp_id: grp_id

        Returns:
        list of all feedbacks
        """
        response = db.get_items(config.queries["VIEW_FEEDBACK"], (grp_id,))
        if response:
            return [
                {"criteria": tup[0], "feedback": tup[1], "comments": tup[2]}
                for tup in response
            ]

        raise BadRequestException("No feedbacks available.")

    @staticmethod
    def get_menu_fdb_criterias(grp_id):
        """
        Retrieves a list of criteria for a given menu

        Args:
          grp_id: Tgrp_id

        Returns:
        feedback criterias for a menu
        """
        response = db.get_items(config.queries["GET_MENU_FDB_CRITERIAS"], (grp_id,))
        if len(response) > 0:
            criterias = [{"cr_id": tup[1], "criteria": tup[2]} for tup in response]
            return criterias

        raise NotFoundException("No criterias have been decided for current menu.")

    @staticmethod
    def add_feedback(feedback):
        """
        Adds feedback to a database.

        """
        _id = db.add_items(config.queries["ADD_FEEDBACK"], feedback)
        if _id:
            return _id
        raise DbException("Could not add feedback")
