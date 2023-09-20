"""
Module which contains the class and associated methods,
to display console menus
"""
import json
import os

import maskpass
from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.InputHelpers import InputHelpers, GetInput
from src.helpers.exceptions import (
    NoSuchUserError,
)
from src.utils import prompts, config


class ChoiceDisplayer:
    """
    Class containing all the required methods,
    to display the console menus
    """
    def __init__(self, user=None):
        self.user = user
        self.helper = None
        with open(r"C:\Users\umani\Desktop\clone\data.json", "r") as file:
            data = json.load(file)
            config.prompts = data["menu_choices"]
            config.queries = data["queries"]

    def entry(self):
        """
        First Method that is called which further,
        calls the login view
        """
        print(prompts.HEADER)
        self.login_view()

    def login_view(self):
        """
        Login View, which asks the user for credentials,
        and accordingly calls the helper functions
        """
        print("Hello, Please login with your credentials!! ")
        user_name = input("Enter user name - ")
        password = maskpass.advpass(prompt="Enter password - ")

        try:
            login_obj = Login()
            is_validated = login_obj.authenticate_credentials(
                user_name=user_name, password=password
            )
        except NoSuchUserError:
            print("No such user found!! Please try again! ")
        else:
            if is_validated:
                self.__initiate_display_choices(user_name)
            else:
                print("Login Failed!! Please input valid credentials!!")
                self.login_view()

    def __admin_view(self):
        os.system("cls")

        self.__notify_not_published_menu()
        self.__notify_rejected_menu()

        while True:
            user_choice = input(config.prompts["ADMIN_CHOICES"])
            if user_choice == "1":
                self.helper.helper_propose_menu()

            elif user_choice == "2":
                self.helper.helper_publish_menu()

            elif user_choice == "3":
                self.helper.helper_set_fdb_criteria()

            elif user_choice == "4":
                self.helper.helper_view_fdb()

            elif user_choice == "5":
                self.user.view_accepted_menu()

            elif user_choice == "6":
                self.__display_rejected_menu_choices()

            elif user_choice == "7":
                print("Thank you, Have a nice day! :) ")
                break

            else:
                print("\n\nInvalid choice, Please try again!!")
                continue

            message = "Do you wish to continue?? (y/n) "
            user_choice = GetInput.get_yesno(message)
            os.system("cls")
            if user_choice == "n":
                print("Thank you, Have a nice day! :) ")
                break

    def __f_emp_view(self):
        self.__notify_pending_menu()

        while True:
            user_choice = input(config.prompts["F_EMP_CHOICES"])
            if user_choice == "1":
                self.helper.helper_validate_user()

            elif user_choice == "2":
                self.helper.helper_receive_order()

            elif user_choice == "3":
                self.helper.helper_accept_menu()

            elif user_choice == "4":
                self.user.view_accepted_menu()

            elif user_choice == "5":
                self.helper.helper_topup_card()

            elif user_choice == "6":
                print("Thank you, Have a nice day! :) ")
                break

            else:
                print("\n\nInvalid choice, Please try again!!")
                continue

            message = "Do you wish to continue?? (y/n) "
            user_choice = GetInput.get_yesno(message)
            os.system("cls")
            if user_choice == "n":
                print("Thank you, Have a nice day! :) ")
                break

    def __emp_view(self):
        while True:
            user_choice = input(config.prompts["EMP_CHOICES"])
            if user_choice == "1":
                self.user.view_accepted_menu()

            elif user_choice == "2":
                self.helper.helper_place_order()

            elif user_choice == "3":
                self.helper.helper_view_balance()

            elif user_choice == "4":
                self.helper.helper_give_feedback()

            elif user_choice == "5":
                print("Thank you, Have a nice day! :) ")
                break

            else:
                print("\n\nInvalid choice, Please try again!!")
                continue

            message = "Do you wish to continue?? (y/n) "
            user_choice = GetInput.get_yesno(message)
            os.system("cls")
            if user_choice == "n":
                print("Thank you, Have a nice day! :) ")
                break

    def __display_choices(self):
        if self.helper.check_role() == "admin":
            self.__admin_choices()
        elif self.helper.check_role() == "f_emp":
            self.__f_emp_view()
        else:
            self.__emp_view()

    def __admin_choices(self):
        user_input = input(config.prompts["VIEW_ADMIN_MENU"])
        while not (user_input != "1" or user_input != "2"):
            user_input = input("\nPlease choose between 1 or 2 - ")

        os.system("cls")
        if user_input == "1":
            self.__admin_view()
        else:
            self.__emp_view()

    def __initiate_display_choices(self, user_name):
        user = User(user_name)
        user.get_details()
        self.user = user
        self.helper = InputHelpers(self.user)
        os.system("cls")
        self.__display_choices()

    def __display_rejected_menu_choices(self):
        is_rejected_response = self.helper.helper_check_rejected_menu()
        if is_rejected_response is None:
            print("There are no rejected menus currently !! Thank you !")
            return

        _menu_id = is_rejected_response[0]
        print(prompts.UPDATE_MENU_TEXT)
        user_choice = input("Enter choice - ")
        while not (user_choice != "1" or user_choice != "2"):
            user_choice = input("Enter valid choice - ")

        if user_choice == "1":
            self.user.discard_menu(_menu_id)
            print("Menu has been discarded! ")

        elif user_choice == "2":
            self.helper.helper_update_menu(_menu_id)

        else:
            print("Please choose between 1 or 2!")

    def __notify_not_published_menu(self):
        is_not_published = self.user.check_menu_status("not published")
        if is_not_published:
            print(config.prompts["MENU_ACCEPTED"])

    def __notify_rejected_menu(self):
        is_rejected_response = self.helper.helper_check_rejected_menu()
        if is_rejected_response is not None:
            comments = is_rejected_response[1]
            print(
                f"\n\n\nYour Menu has been rejected!"
                f"\nReason - {comments if comments != '' else 'No comments'}"
            )

    def __notify_pending_menu(self):
        is_pending = self.user.check_menu_status("pending")
        if is_pending:
            print("\n\nThere are pending menus!! Please review!!!")
