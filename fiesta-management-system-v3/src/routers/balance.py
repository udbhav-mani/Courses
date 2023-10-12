"""
FastAPI router with three endpoints for updating and retrieving user and
group balances.
"""
from typing import Annotated
import logging
from fastapi import (
    status,
    APIRouter,
    Request,
    Body,
    Query,
)

from src.helpers import (
    validate_body,
    grant_access,
    log,
    NoSuchUserError,
    handle_errors,
    get_token,
    UpdateGrpBalanceSchema,
    UpdateUserBalanceSchema,
)
from src.controllers import Account
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


@router.put("/balance/user", status_code=status.HTTP_200_OK)
@validate_body(UpdateUserBalanceSchema)
@grant_access
@log(logger=logger)
def put_balance(request: Request, body: Annotated[dict, Body()]):
    """
    Updates the balance of an account with the specified amount for the given
    user ID.

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()])


    Returns:
      a dictionary with the keys "message", "amount", and "user_id".
    """
    account = Account()
    account.update_balance(amount=body["amount"], user_id=body["user_id"])
    return {
        "message": prompts.get("SUCCESS_MESSAGE"),
        "amount": body["amount"],
        "user_id": body["user_id"],
    }


@router.put("/balance/grp", status_code=status.HTTP_200_OK)
@validate_body(UpdateGrpBalanceSchema)
@grant_access
@log(logger=logger)
def put_grp_balance(request: Request, body: Annotated[dict, Body()]):
    """
    Updates the balance of a specific group.

    Args:
      request (Request): FASTAPI request abject.
      body (Annotated[dict, Body()])

    Returns:
      a dictionary with the keys "message", "amount", and "grp_id".
    """
    account = Account()
    account.update_balance(amount=body["amount"], grp_id=body["grp_id"])
    return {
        "message": prompts.get("SUCCESS_MESSAGE"),
        "amount": body["amount"],
        "grp_id": body["grp_id"],
    }


@router.get("/balance", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
@handle_errors
def get_balance(request: Request, user_id: Annotated[int | None, Query()]):
    """
    Retrieves the balance of a user's account
    
    Args:
      request (Request):FASTAPI request abject
      user_id (Annotated[int | None, Query()]): user_id of user
    
    Returns:
      a dictionary with the following keys and values:
    - "id": user_id 
    - "balance": balance 
    - "grp_id": the "grp_id" of group.
    """
    account = Account()
    try:
        balance = account.view_balance(user_id=user_id)
    except NoSuchUserError as err:
        raise NoSuchUserError(str(err)) from err

    return {
        "id": user_id,
        "balance": balance,
        "grp_id": get_token(request=request).get("grp_id"),
    }
