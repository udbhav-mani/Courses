import logging
from src.helpers.jwt_helper import get_token
from fastapi import APIRouter, Request, Body, status, Query, Path
from typing import Annotated
from src.helpers import grant_access, validate_body, log, handle_errors
from datetime import datetime
import starlette


from src.controllers.account import Account
from src.controllers.menu import Menu
from src.schemas import MenuSchema, UpdateSchema, UpdateItemSchema
from src.helpers.exceptions import error, BadRequestException
from enum import Enum

logger = logging.getLogger(__name__)
router = APIRouter()


class Status(str, Enum):
    published = "published"
    pending = "pending"
    not_published = "not_published"
    rejected = "rejected"


@router.get("/menu", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
@handle_errors
def get_menu(request: Request, status: Annotated[Status, Query()]):
    grp_id = get_token(request=request).get("grp_id")
    menu = Menu()

    if status is status.published:
        response = menu.view_accepted_menu(grp_id=grp_id)
    else:
        response = menu.get_menu_by_status(grp_id=grp_id, status=status)

    if len(response) == 0:
        raise BadRequestException("No such menu found.")
    else:
        date = response[0][1]
        items = [item[0] for item in response]
        return dict(menu_id=response[0][2], date=date, items=items)


@router.post("/menu", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(MenuSchema)
@log(logger=logger)
def post_menu(request: Request, body: Annotated[dict, Body()]):
    name = get_token(request=request).get("username")
    grp_id = get_token(request=request).get("grp_id")

    items = body["items"]
    date = body["date"]
    datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

    menu = Menu()
    response = menu.propose_menu(items, datetime_object, name, grp_id)
    return dict(message=response)


@log(logger=logger)
@grant_access
@validate_body(UpdateSchema)
@router.put("/menu", status_code=status.HTTP_200_OK)
def put_menu(request: Request, body: Annotated[dict, Body()]):
    grp_id = get_token(request=request).get("grp_id")
    menu = Menu()
    menu_id = body["menu_id"]
    status = body["status"]

    if status == "published":
        response = menu.get_menu_by_status(grp_id=grp_id, status="not published")
        date = response[0][1]
        menu.publish_menu(menu_id=menu_id, grp_id=grp_id, menu_date=date)
        account = Account()
        account.update_balance(amount=137, grp_id=grp_id)
        return dict(message="success")

    elif status == "rejected":
        comments = body["comments"]
        username = get_token(request=request).get("username")
        menu.reject_menu(menu_id=menu_id, comments=comments, username=username)
        return dict(message="success")
    else:
        menu.update_menu_status(status, menu_id)
        return dict(message="success")


@router.patch("/menu/{menu_id}", status_code=status.HTTP_200_OK)
@validate_body(UpdateItemSchema)
@grant_access
@log(logger=logger)
def patch_menu(
    request: Request, body: Annotated[dict, Body()], menu_id: Annotated[int, Path()]
):
    menu = Menu()
    menu.update_menu(
        menu_id=menu_id, old_item=body["old_item"], new_item=body["new_item"]
    )
    return dict(message="success", new_item=body["new_item"], menu_id=menu_id)
