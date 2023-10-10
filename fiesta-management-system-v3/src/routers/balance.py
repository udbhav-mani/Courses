import logging
from src.helpers.schemas.schemas import UpdateGrpBalanceSchema, UpdateUserBalanceSchema
from fastapi import (
    status,
    APIRouter,
    Request,
    Body,
    Query,
)
from typing import Annotated

from src.helpers import (
    validate_body,
    grant_access,
    log,
    NoSuchUserError,
    handle_errors,
    get_token,
)
from src.controllers import Account

logger = logging.getLogger(__name__)
router = APIRouter()


@router.put("/balance/user", status_code=status.HTTP_200_OK)
@validate_body(UpdateUserBalanceSchema)
@grant_access
@log(logger=logger)
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
@log(logger=logger)
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
@log(logger=logger)
@handle_errors
def get_balance(request: Request, user_id: Annotated[int | None, Query()]):
    account = Account()
    try:
        balance = account.view_balance(user_id=user_id)
    except NoSuchUserError as err:
        raise NoSuchUserError(str(err))
    else:
        return {
            "id": user_id,
            "balance": balance,
            "grp_id": get_token(request=request).get("grp_id"),
        }
