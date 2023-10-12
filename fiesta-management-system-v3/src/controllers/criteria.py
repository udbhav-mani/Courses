"""
Provides Criteria class for operations related to feedback criterias
"""
import logging

from src.models.database import Database
from src.utils import config
from src.helpers import log


logger = logging.getLogger(__name__)


class Criteria:
    """
    Provides methods for setting feedback criteria, getting feedback criteria, and
    adding new criteria to a database.
    """

    @log(logger=logger)
    def set_fdb_criteria(self, criterias_selected, grp_id):
        """
        Sets feedback criteria for a given menu.

        Args:
          -criterias_selected: criterias to be set
          -grp_id
        """
        db = Database()
        response = db.get_item(
            config.queries["SET_FEEDBACK_CRITERIA_QUERY1"], (grp_id,)
        )
        _menu_id = response[0]
        cr_id_list = []
        for criteria in criterias_selected["criteria"]:
            response = db.get_item(
                config.queries["SET_FEEDBACK_CRITERIA_QUERY2"], (criteria,)
            )
            _cr_id = response[0]
            cr_id_list.append(_cr_id)

        data_list = [(_menu_id, cr_id) for cr_id in cr_id_list]
        db.add_items(config.queries["SET_FEEDBACK_CRITERIA_QUERY3"], data_list)

    @staticmethod
    @log(logger=logger)
    def get_fdb_criteria():
        """
        Retrieves criteria from the list of criterias.
        
        Returns:
        criterias for the feedback
        """
        db = Database()
        response = db.get_items(config.queries["GET_FDB_CRITERIAS"], data=None)
        criteria = [{"id": line[0], "criteria": line[1]} for line in response]
        return criteria

    @staticmethod
    @log(logger=logger)
    def add_new_criteria(new_criteria):
        """
        Adds new criteria to a list of criterias.
        
        Args:
          new_criteria: new criterias to be added
        """
        db = Database()
        data_tuple = [(criteria,) for criteria in new_criteria]
        db.add_items(config.queries["UPDATE_CRITERIA"], data_tuple)
