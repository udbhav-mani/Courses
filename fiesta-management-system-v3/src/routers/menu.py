from helpers.jwt_helper import get_token
from fastapi import APIRouter, Request, Body, status, Query, Path
from typing import Annotated
from src.helpers.decorators import grant_access, validate_body
from fastapi.responses import JSONResponse
from datetime import datetime
import starlette


from src.controllers.account import Account
from src.controllers.menu import Menu
from src.schemas import MenuSchema, UpdateSchema, UpdateItemSchema
from src.helpers.exceptions import error
from enum import Enum

router = APIRouter()
logger = logging.getLogger(__name__)


class Status(str, Enum):
    published = "published"
    pending = "pending"
    not_published = "not_published"
    rejected = "rejected"


@router.get("/menu", status_code=status.HTTP_200_OK)
def get_menu(request: Request, status: Annotated[Status, Query()]):
    grp_id = get_token(request=request).get("grp_id")
    menu = Menu()

    if status is status.published:
        response = menu.view_accepted_menu(grp_id=grp_id)
    else:
        response = menu.get_menu_by_status(grp_id=grp_id, status=status)

    if len(response) == 0:
        return JSONResponse(
            status_code=starlette.status.HTTP_400_BAD_REQUEST,
            content=error(
                code=404,
                message="No such menu found.",
            ),
        )
    else:
        print(response)
        date = response[0][1]
        items = [item[0] for item in response]
        return dict(menu_id=response[0][2], date=date, items=items)


@router.post("/menu", status_code=status.HTTP_201_CREATED)
@grant_access(["admin"])
@validate_body(MenuSchema)
def post_menu(request: Request, body: Annotated[dict, Body()]):
    menu = Menu()
    items = body["items"]
    name = get_token(request=request).get("username")
    grp_id = get_token(request=request).get("grp_id")
    date = body["date"]
    datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    response = menu.propose_menu(items, datetime_object, name, grp_id)
    return dict(message=response)


@router.put("/menu", status_code=status.HTTP_200_OK)
@grant_access(["admin", "f_emp"])
@validate_body(UpdateSchema)
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
        response = menu.reject_menu(
            menu_id=menu_id, comments=comments, username=username
        )
        return dict(message=response)
    else:
        response = menu.update_menu_status(status, menu_id)
        return dict(message=response)


@router.patch("/menu/{menu_id}", status_code=status.HTTP_200_OK)
@grant_access(roles_allowed=["admin", "f_emp"])
@validate_body(UpdateItemSchema)
def patch_menu(
    request: Request, body: Annotated[dict, Body()], menu_id: Annotated[int, Path()]
):
    menu = Menu()
    menu.update_menu(
        menu_id=menu_id, old_item=body["old_item"], new_item=body["new_item"]
    )
    return dict(message="success", new_item=body["new_item"], menu_id=menu_id)
