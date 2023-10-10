import logging
from fastapi import APIRouter, Request, Body, status
from typing import Annotated

from src.helpers import grant_access, validate_body, log
from src.controllers import Criteria
from src.helpers.schemas.schemas import CriteriaSchema

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/criterias", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
def get_criteria(request: Request):
    criteria = Criteria()
    response = criteria.get_fdb_criteria()
    return response


@router.post("/criterias", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(CriteriaSchema)
@log(logger=logger)
def post_criteria(request: Request, body: Annotated[dict, Body()]):
    criteria = Criteria()
    criteria.add_new_criteria(body["criteria"])
    return dict(message="Criteria added successfully", status="success")
