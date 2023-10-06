from helpers.jwt_helper import get_token
from fastapi import APIRouter, Request, Body, Query, Path
from typing import Annotated
from src.helpers.decorators import validate_body
from src.controllers.user import User

from src.schemas import OrderSchema

router = APIRouter()


@router.post("/orders")
@validate_body(OrderSchema)
def place_order(request: Request, body: Annotated[dict, Body()]):
    user = User()
    user.update_balance(amount=-1 * body["amount"], user_id=body["user_id"])
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


@router.get("/orders/{user_id}")
def get_order(
    user_id: Annotated[int, Path()], date: Annotated[str | None, Query()] = None
):
    user = User()
    if date is None:
        data = user.check_order(user_id=user_id)
        return data
    else:
        data = user.check_order(user_id=user_id, date=date)
        return data
