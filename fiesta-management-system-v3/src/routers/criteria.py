from fastapi import APIRouter, Request, Body, status
from typing import Annotated
from src.helpers.decorators import grant_access, validate_body
from src.helpers.decorators import grant_access, validate_body
from src.controllers.criteria import Criteria
from src.schemas import CriteriaSchema

router = APIRouter()


@router.get("/criterias", status_code=status.HTTP_200_OK)
@grant_access(roles_allowed=["admin", "emp"])
def get_criteria(request: Request):
    criteria = Criteria()
    response = criteria.get_fdb_criteria()
    return response


@router.post("/criterias", status_code=status.HTTP_201_CREATED)
@grant_access(roles_allowed=["admin", "emp"])
@validate_body(CriteriaSchema)
def post_criteria(request: Request, body: Annotated[dict, Body()]):
    criteria = Criteria()
    criteria.add_new_criteria(body["criteria"])
    return dict(message="Criteria added successfully", status="success")
