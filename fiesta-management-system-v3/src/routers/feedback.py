import logging
from fastapi import APIRouter, Request, Body, status, Query
from typing import Annotated

from src.helpers.schemas.schemas import PlainFeedbackSchema, CriteriaSchema
from src.helpers import grant_access, validate_body, log, handle_errors, get_token, NotFoundException
from src.controllers import User, Menu, Feedback, Criteria

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/feedback/criterias", status_code=status.HTTP_200_OK)
@log(logger=logger)
@grant_access
@handle_errors
def get_fdb_criterias(request: Request):
    grp_id = get_token(request=request).get("grp_id")
    try:
        response = User.get_menu_fdb_criterias(grp_id)
    except NotFoundException as err:
        raise NotFoundException(str(err))
    else:
        return response


@router.post("/feedback/criterias", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(CriteriaSchema)
@log(logger=logger)
def post_fdb_criterias(request: Request, body: Annotated[dict, Body()]):
    criteria = Criteria()
    criteria.set_fdb_criteria(
        criterias_selected=body, grp_id=get_token(request=request).get("grp_id")
    )
    return dict(criterias=body, grp_id=get_token(request=request).get("grp_id"))


@router.get("/feedback", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
def get_fdbs(request: Request, criteria: Annotated[str | None, Query()] = None):
    feedback = Feedback()
    response = feedback.view_all_feedbacks(get_token(request=request).get("grp_id"))

    if criteria:
        filtered_response = []
        for item in response:
            if item.get("criteria") == criteria:
                filtered_response.append(item)
        return filtered_response

    return response


@router.post("/feedback", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(PlainFeedbackSchema)
@log(logger=logger)
def post_feedback(request: Request, body: Annotated[list[dict], Body()]):
    user_id = get_token(request=request).get("user_id")
    grp_id = get_token(request=request).get("grp_id")
    menu_id = Menu.get_menu_from_group(grp_id)
    var = [
        (user_id, item["cr_id"], menu_id, int(item["feedback"]), item["comments"])
        for item in body
    ]
    User.add_feedback(var)
    return dict(message="success")
