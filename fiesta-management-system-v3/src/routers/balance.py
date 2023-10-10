from src.schemas import UpdateGrpBalanceSchema, UpdateUserBalanceSchema
from src.helpers.exceptions import error
from fastapi import (
    HTTPException,
    status,
    APIRouter,
    Request,
    Body,
    Query,
)

from typing import Annotated
from src.helpers.jwt_helper import get_token
from src.helpers import validate_body, grant_access
from src.controllers.user import Account


router = APIRouter()


@router.put("/balance/user", status_code=status.HTTP_200_OK)
@validate_body(UpdateUserBalanceSchema)
@grant_access
def put_balance(request: Request, body: Annotated[dict, Body()]):
    account = Account()
    account.update_balance(amount=body["amount"], user_id=body["user_id"])
    return {
        "message": "success",
        "amount": body["amount"],
        "user_id": body["user_id"],
    }


@router.put("/balance/grp", status_code=status.HTTP_200_OK)
@validate_body(UpdateGrpBalanceSchema)
@grant_access
def put_grp_balance(request: Request, body: Annotated[dict, Body()]):
    account = Account()
    account.update_balance(amount=body["amount"], grp_id=body["grp_id"])
    return {
        "message": "success",
        "amount": body["amount"],
        "grp_id": body["grp_id"],
    }


@router.get("/balance", status_code=status.HTTP_200_OK)
@grant_access
def get_balance(request: Request, user_id: Annotated[int | None, Query()]):
    account = Account()
    balance = account.view_balance(user_id=user_id)
    if balance:
        return {
            "id": user_id,
            "balance": balance,
            "grp_id": get_token(request=request).get("grp_id"),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error(code=404, message="No such user found."),
        )
