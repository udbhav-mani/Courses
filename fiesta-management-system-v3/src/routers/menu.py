"""
FastAPI router with various
endpoints for managing menus, including getting
menus, creating menus, updating menus, and patching menus.
"""
from datetime import datetime
import logging
from typing import Annotated
from enum import Enum
from fastapi import APIRouter, Request, Body, status, Query, Path

from src.controllers import Account, Menu
from src.helpers import (
    BadRequestException,
    grant_access,
    validate_body,
    log,
    handle_errors,
    get_token,
    MenuSchema,
    UpdateSchema,
    UpdateItemSchema,
    NoMenuFoundError,
)
from src.utils.config import prompts

logger = logging.getLogger(__name__)
router = APIRouter()


class Status(str, Enum):
    """
    Defines an enumeration for different statuses
    """

    PUBLISHED = "published"
    PENDING = "pending"
    NOT_PUBLISHED = "not published"
    REJECTED = "rejected"


@router.get("/menu", status_code=status.HTTP_200_OK)
@grant_access
@log(logger=logger)
@handle_errors
def get_menu(request: Request, status: Annotated[Status, Query()]):
    """
    Retrieves a menu based on the status and group ID provided in the request.

    Args:
      request (Request): FASTAPI request abject
      status (Annotated[Status, Query()]):
      - It represents the status of the menu items that should be returned.

    Returns:
      the result of the "__menu_response" function, which is not shown in the provided code.
    """
    grp_id = get_token(request=request).get("grp_id")
    menu = Menu()

    if status is status.PUBLISHED:
        response = menu.view_accepted_menu(grp_id=grp_id)

    else:
        response = menu.get_menu_by_status(grp_id=grp_id, status=status)

    return __menu_response(response)


@router.post("/menu", status_code=status.HTTP_201_CREATED)
@grant_access
@validate_body(MenuSchema)
@handle_errors
@log(logger=logger)
def post_menu(request: Request, body: Annotated[dict, Body()]):
    """
    Checks if there is already a menu in pending or rejected state and returns
    an error message if so, otherwise it adds the menu

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()]): body dictionary
    Returns:
      - a BadRequestException
      - or success message
    """

    name = get_token(request=request).get("username")
    grp_id = get_token(request=request).get("grp_id")
    items = body["items"]
    date = body["date"]
    pending, rejected = None, None

    menu = Menu()
    try:
        pending = menu.get_menu_by_status(grp_id=grp_id, status="pending")
        rejected = menu.get_menu_by_status(grp_id=grp_id, status="rejected")
    except NoMenuFoundError:
        pass

    if not pending and not rejected:
        return __propose_menu_helper(items, date, name, grp_id)

    raise BadRequestException(prompts.get("MENU_ALREADY_PENDING_REJECTED"))


@router.put("/menu", status_code=status.HTTP_200_OK)
@log(logger=logger)
@grant_access
@handle_errors
@validate_body(UpdateSchema)
def put_menu(request: Request, body: Annotated[dict, Body()]):
    """
    Updates the status of a menu based on the provided parameters.

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()])

    Returns:
      a dictionary with a key "message" and a value "success".
    """
    grp_id = get_token(request=request).get("grp_id")
    menu = Menu()
    menu_id = body["menu_id"]
    menu_status = body["status"]
    username = get_token(request=request).get("username")

    if menu_status == "published":
        return __publish_menu(grp_id=grp_id, menu_id=menu_id)

    if menu_status == "rejected":
        comments = body["comments"]
        return __reject_menu(menu_id=menu_id, comments=comments, username=username)

    menu.update_menu_status(menu_status, menu_id)
    return {"message": prompts.get("SUCCESS_MESSAGE")}


@router.patch("/menu/{menu_id}", status_code=status.HTTP_200_OK)
@validate_body(UpdateItemSchema)
@grant_access
@handle_errors
@log(logger=logger)
def patch_menu(
    request: Request, body: Annotated[dict, Body()], menu_id: Annotated[int, Path()]
):
    """
    Updates a menu item in a menu.

    Args:
      request (Request): FASTAPI request abject
      body (Annotated[dict, Body()]):
      - dictionary that contains the request body data.
      menu_id (Annotated[int, Path()]):  menu_id

    Returns:
      a dictionary with the keys "message", "new_item", and "menu_id".
    """
    menu = Menu()
    menu.update_menu(
        menu_id=menu_id, old_item=body["old_item"], new_item=body["new_item"]
    )
    return {
        "message": prompts.get("SUCCESS_MESSAGE"),
        "new_item": body["new_item"],
        "menu_id": menu_id,
    }


def __publish_menu(grp_id, menu_id):
    """
    Publishes a menu and  updates the account balance

    Args:
      grp_id: Used to identify the group
      menu_id: The menu_id of the menu.

    Returns: a dictionary with a key "message" and a value "success".
    """
    menu = Menu()
    response = menu.get_menu_by_status(grp_id=grp_id, status="not published")
    date = response[0][1]
    menu.publish_menu(menu_id=menu_id, grp_id=grp_id, menu_date=date)
    account = Account()
    account.update_balance(amount=137, grp_id=grp_id)
    return {"message": prompts.get("SUCCESS_MESSAGE")}


def __reject_menu(menu_id, comments, username):
    """
    Rejects a menu with the given menu ID, comments, and username.
    """
    menu = Menu()
    menu.reject_menu(menu_id=menu_id, comments=comments, username=username)
    return {"message": prompts.get("SUCCESS_MESSAGE")}


def __menu_response(response):
    """
    Extracts the date and items from the response, and returns a
    dictionary with the menu ID, date, and items.
    """
    date = response[0][1]
    items = [item[0] for item in response]
    return {"menu_id": response[0][2], "date": date, "items": items}


def __propose_menu_helper(items, date, name, grp_id):
    """
    Adds a menu to a group with the specified items, date, name, and
    group ID.
    """
    datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    menu = Menu()
    menu.propose_menu(items, datetime_object, name, grp_id)
    return {"message": prompts.get("SUCCESS_MESSAGE")}
