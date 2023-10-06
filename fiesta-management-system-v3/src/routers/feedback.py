from helpers.jwt_helper import get_token
from src.controllers.feedback import Feedback
from src.controllers.menu import Menu
from src.controllers.user import User
from src.schemas import PlainFeedbackSchema
from src.helpers.exceptions import error
from fastapi import APIRouter, Request, Body, status, Query
from typing import Annotated
from src.helpers.decorators import grant_access, validate_body
from src.controllers.criteria import Criteria
from src.schemas import CriteriaSchema
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/feedback/criterias", status_code=status.HTTP_200_OK)
def get_fdb_criterias():
    grp_id = get_token().get("grp_id")
    response = User.get_menu_fdb_criterias(grp_id)
    if response is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=error(
                code=400, message="No criterias have been decided for current menu."
            ),
        )
    return response


@router.post("/feedback/criterias", status_code=status.HTTP_201_CREATED)
@grant_access(["admin"])
@validate_body(CriteriaSchema)
def post_fdb_criterias(request: Request, body: Annotated[dict, Body()]):
    criteria = Criteria()
    criteria.set_fdb_criteria(
        criterias_selected=body, grp_id=get_token(request=request).get("grp_id")
    )
    return dict(criterias=body, grp_id=get_token(request=request).get("grp_id"))


@router.get("/feedback", status_code=status.HTTP_200_OK)
@grant_access(["admin", "emp"])
def get_fdbs(request: Request, criteria: Annotated[int | None, Query()]):
    feedback = Feedback()
    response = feedback.view_all_feedbacks(get_token(request=request).get("grp_id"))
    if criteria is not None:
        filtered_response = []
        for item in response:
            if item.get("criteria") == criteria:
                filtered_response.append(item)
        return filtered_response
    return response


@router.post("/feedback", status_code=status.HTTP_201_CREATED)
@grant_access(["admin", "emp"])
@validate_body(PlainFeedbackSchema)
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
