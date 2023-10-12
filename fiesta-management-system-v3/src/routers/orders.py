"""
Defines two API endpoints for placing an order and retrieving order data for a
specific user.

"""
from typing import Annotated
import logging
from fastapi import APIRouter, Request, Body, Query, Path, status

from src.helpers import (
    validate_body,
    grant_access,
    log,
    handle_errors,
    BadRequestException,
    get_token,
    OrderSchema,
)
from src.controllers import User
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
@validate_body(OrderSchema)
@grant_access
@log(logger=logger)
@handle_errors
def place_order(request: Request, body: Annotated[dict, Body()]):
    """
    Processes a user's order by checking their balance, updating their
    balance, and storing the order details.

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()])

    Returns:
      a dictionary with the following keys and values:
    - "message": "success"
    - "amount": amount updated
    - "order_id": the order_id generated.
    """
    user = User()
    user_id = body["user_id"]
    amount = body["amount"]
    balance = user.view_balance(user_id=user_id)
    if amount > balance:
        raise BadRequestException(prompts.get("AMOUNT_INVALID"))

    user.update_balance(amount=-1 * amount, user_id=user_id)
    order_id = User.store_order(
        amount=body["amount"],
        user_id=body["user_id"],
        created_by=get_token(request=request).get("username"),
    )
    return {
        "message": prompts.get("SUCCESS_MESSAGE"),
        "amount": body["amount"],
        "order_id": order_id,
    }


@router.get("/orders/{user_id}", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
def get_order(
    request: Request,
    user_id: Annotated[int, Path()],
    date: Annotated[str | None, Query()] = None,
):
    """
    Retrieves order data for a specific user,
    either for a specific date or for
    all dates if no date is provided.

    Args:
      request (Request): FASTAPI request abject
      user_id (Annotated[int, Path()]): user_id of user
      date (Annotated[str | None, Query()]): date (optional) for filtering

    Returns:
    data of the order for the specified user.
    ALso filters on basis of date
    """
    user = User()
    if date is None:
        data = user.check_order(user_id=user_id)
        return data

    data = user.check_order(user_id=user_id, date=date)
    return data
