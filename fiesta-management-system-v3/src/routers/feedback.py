"""
FastAPI router with various endpoints for managing feedback and criteria,
including retrieving criteria, creating criteria, retrieving feedback, and creating feedback.
"""
from typing import Annotated
import logging
from fastapi import APIRouter, Request, Body, status, Query

from src.helpers import (
    grant_access,
    validate_body,
    log,
    handle_errors,
    get_token,
    NotFoundException,
    PlainFeedbackSchema,
    CriteriaSchema,
)
from src.controllers import User, Menu, Feedback, Criteria
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/feedback/criterias", status_code=status.HTTP_200_OK)
@log(logger=logger)
@grant_access
@handle_errors
def get_fdb_criterias(request: Request):
    """
    Retrieves menu FDB criterias for a given group ID.

    Args:
      request (Request): FASTAPI request abject

    Returns:
      Feedback criterias for a menu.
    """
    grp_id = get_token(request=request).get("grp_id")
    try:
        response = User.get_menu_fdb_criterias(grp_id)
    except NotFoundException as err:
        raise NotFoundException(str(err)) from err

    return response


@router.post("/feedback/criterias", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(CriteriaSchema)
@log(logger=logger)
def post_fdb_criterias(request: Request, body: Annotated[dict, Body()]):
    """
    Sets FDB criteria based on the provided request and body.

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()])

    Returns:
    a dictionary with two keys: "criterias" and "grp_id".
    """
    criteria = Criteria()
    criteria.set_fdb_criteria(
        criterias_selected=body, grp_id=get_token(request=request).get("grp_id")
    )
    return {"criterias": body, "grp_id": get_token(request=request).get("grp_id")}


@router.get("/feedback", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
@handle_errors
def get_fdb(request: Request, criteria: Annotated[str | None, Query()] = None):
    """
    Retrieves feedback data and also filters it based on criteria.

    Args:
      request (Request): FASTAPI request abject
      criteria (Annotated[str | None, Query()]): criteria for filtering feedbacks (optional)

    Returns:
    If the 'criteria' parameter is provided, the
    function returns a filtered response based on the criteria.
    If the 'criteria' parameter is not
    provided, the function returns all the feedbacks on a menu.
    """
    feedback = Feedback()
    response = feedback.view_all_feedbacks(get_token(request=request).get("grp_id"))

    if criteria:
        return __get_filtered_response(response, criteria)

    return response


@router.post("/feedback", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(PlainFeedbackSchema)
@log(logger=logger)
@handle_errors
def post_fdb(request: Request, body: Annotated[list[dict], Body()]):
    """
    Extracts user and group IDs from the request and
    adds feedback.

    Args:
      request (Request):FASTAPI request abject
      body (Annotated[list[dict], Body()])

    """
    user_id = get_token(request=request).get("user_id")
    grp_id = get_token(request=request).get("grp_id")
    return __post_feedback_helper(user_id, grp_id, body)


def __get_filtered_response(response, criteria):
    """
    Filters a response based on a given criteria.
    """
    filtered_response = []
    for item in response:
        if item.get("criteria") == criteria:
            filtered_response.append(item)
    return filtered_response


def __post_feedback_helper(user_id, grp_id, body):
    """
    Adds feedback from users to a menu item.
    """
    menu_id = Menu.get_menu_from_group(grp_id)
    var = [
        (user_id, item["cr_id"], menu_id, int(item["feedback"]), item["comments"])
        for item in body
    ]
    User.add_feedback(var)
    return {"message": prompts.get("SUCCESS_MESSAGE")}
