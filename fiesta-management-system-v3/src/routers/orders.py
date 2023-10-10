import logging
from src.helpers.exceptions import BadRequestException
from src.helpers.jwt_helper import get_token
from fastapi import APIRouter, Request, Body, Query, Path, status
from typing import Annotated
from src.helpers import validate_body, grant_access, log, handle_errors
from src.controllers.user import User

from src.schemas import OrderSchema

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
@validate_body(OrderSchema)
@grant_access
@log(logger=logger)
@handle_errors
def place_order(request: Request, body: Annotated[dict, Body()]):
    user = User()
    user_id = body["user_id"]
    amount = body["amount"]
    balance = user.view_balance(user_id=user_id)
    if amount > balance:
        raise BadRequestException("Amount is greater than current balance.")

    user.update_balance(amount=-1 * amount, user_id=user_id)
    order_id = User.store_order(
        amount=body["amount"],
        user_id=body["user_id"],
        created_by=get_token(request=request).get("username"),
    )
    return {
        "message": "success",
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
    user = User()
    if date is None:
        data = user.check_order(user_id=user_id)
        return data
    else:
        data = user.check_order(user_id=user_id, date=date)
        return data
