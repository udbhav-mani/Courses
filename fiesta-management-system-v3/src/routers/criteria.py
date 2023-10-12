"""
API endpoints for getting and adding criteria for feedback
"""
from typing import Annotated
import logging
from fastapi import APIRouter, Request, Body, status

from src.helpers import grant_access, validate_body, log, CriteriaSchema
from src.controllers import Criteria
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/criterias", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
def get_criteria(request: Request):
    """
    Returns all criterias.

    Args:
      request (Request):FASTAPI request abject

    Returns:
      All the criterias
    """
    criteria = Criteria()
    response = criteria.get_fdb_criteria()
    return response


@router.post("/criterias", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(CriteriaSchema)
@log(logger=logger)
def post_criteria(request: Request, body: Annotated[dict, Body()]):
    """
    Adds new criteria to an existing set of criteria

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()])

    Returns:
      A dictionary with two key-value pairs: "message" and "status".
    """
    criteria = Criteria()
    criteria.add_new_criteria(body["criteria"])
    return {
        "message": prompts.get("CRITERIA_SUCCESS_MESSAGE"),
        "status": prompts.get("SUCCESS_MESSAGE")
    }
