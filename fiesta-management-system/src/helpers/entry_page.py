import datetime
import os

import maskpass
from prettytable import PrettyTable
from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.exceptions import (
    NoSuchUserError,
    NoMenuFoundError,
    AccessDeniedException,
)
from src.helpers.validators import Validators
from src.models.database import Database
from src.utils import prompts, queries


class ChoiceDisplayer:
    def __init__(self, user=None):
        self.user = user
        self.helper = None

    def entry(self):
        print(prompts.HEADER)
        self.login_view()

    def login_view(self):
        print("Hello, Please login with your credentials!! ")
        user_name = input("Enter user name - ")
        password = maskpass.advpass(prompt="Enter password - ")

        login_obj = Login(user_name=user_name, password=password)

        try:
            is_validated = login_obj.authenticate_credentials()
        except NoSuchUserError:
            print("No such user found!! Please try again! ")
        else:
            if is_validated:
                user = User(user_name)
                user.get_details()
                self.user = user
                self.helper = Helpers(self.user)
                os.system("cls")
                self.display_choices()
            else:
                print("Login Failed!! Please input valid credentials!!")
                self.login_view()

    def admin_view(self):
        os.system("cls")
        is_not_published = self.user.check_menu_status("not published")
        if is_not_published:
            print(queries.MENU_ACCEPTED)

        is_rejected_response = self.helper.check_rejected_menu()
        if is_rejected_response is not None:
            _menu_id = is_rejected_response[0]
            comments = is_rejected_response[1]
            print(
                f"\n\n\nYour Menu has been rejected!"
                f"\nReason - {comments if comments != '' else 'No comments'}"
            )

            print(prompts.UPDATE_MENU_TEXT)
            user_choice = input("Enter choice - ")
            while not (user_choice != "1" or user_choice != "2"):
                user_choice = input("Enter valid choice - ")

            if user_choice == "1":
                self.user.discard_menu(_menu_id)
                print("Menu has been discarded! ")
            elif user_choice == "2":
                print("Current Menu - ")
                response = self.user.view_menu(_menu_id)
                items_dict = {}
                for index, tup in enumerate(response, start=1):
                    items_dict[index] = tup[0]

                item_number = int(input("Enter the item number you want to change - "))
                while item_number not in range(1, len(items_dict) + 1):
                    item_number = int(input("Please enter valid item number - "))

                old_item = items_dict.get(item_number)
                new_item = GetInput.get_input("Enter the new item name - ")

                self.user.update_menu(
                    _menu_id,
                    old_item,
                    new_item,
                )
                print("Menu updated succesfully ! ")
            else:
                print("Please choose between 1 or 2!")

        while True:
            user_choice = input(prompts.ADMIN_CHOICES)
            if user_choice == "1":
                self.helper.propose_menu()
            elif user_choice == "2":
                self.helper.publish_menu()
            elif user_choice == "3":
                self.helper.set_fdb_criteria()
            elif user_choice == "4":
                self.helper.view_fdb()
            elif user_choice == "5":
                try:
                    self.user.view_accepted_menu()
                except AccessDeniedException as e:
                    print(e)
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

    def f_emp_view(self):
        is_pending = self.user.check_menu_status("pending")
        if is_pending:
            print("\n\n!!! There are pending menus!! Please review!!!")

        while True:
            user_choice = input(prompts.F_EMP_CHOICES)
            if user_choice == "1":
                self.helper.validate_user()
            elif user_choice == "2":
                self.helper.receive_order()
            elif user_choice == "3":
                self.helper.accept_menu()
            elif user_choice == "4":
                try:
                    self.user.view_accepted_menu()
                except AccessDeniedException as e:
                    print(e)

            elif user_choice == "5":
                self.helper.topup_card()
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

    def emp_view(self):
        while True:
            user_choice = input(prompts.EMP_CHOICES)
            if user_choice == "1":
                try:
                    self.user.view_accepted_menu()
                except AccessDeniedException as e:
                    print(e)
            elif user_choice == "2":
                self.user.place_order()
            elif user_choice == "3":
                self.helper.view_balance()
            elif user_choice == "4":
                self.helper.give_feedback()
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

    def display_choices(self):
        if self.helper.check_role() == "admin":
            self.choose_for_admin()
        elif self.helper.check_role() == "f_emp":
            self.f_emp_view()
        else:
            self.emp_view()

    def choose_for_admin(self):
        user_input = input(prompts.VIEW_ADMIN_MENU)
        while not (user_input != "1" or user_input != "2"):
            user_input = input("\nPlease choose between 1 or 2 - ")
        if user_input == "1":
            os.system("cls")
            self.admin_view()
        elif user_input == "2":
            os.system("cls")
            self.emp_view()
        else:
            print("\n\nPlease choose between 1 or 2 ")
            self.choose_for_admin()


class Helpers:
    """
    Helper class to help the entry views to interact with the user
    as well as the controllers
    """

    def __init__(self, user=None):
        """Assigns the user to Helpers class on instantiation"""
        self.user = user

    def check_role(self):
        """returns role of user"""
        return self.user.role

    def topup_card(self):
        """Helps with taking inputs
        - validates user first
        - calls update balance()"""
        user_id = input("Enter user_id - ")
        is_validated = self.user.validate_user(user_id=user_id)
        if is_validated:
            user_input = int(input("Enter the amount you want to add to card - "))
            while user_input not in range(0, 20000):
                user_input = int(input("Enter valid amount (0-20000) - "))
            self.user.update_balance(user_id=user_id, amount=user_input)
            print(f"{user_input} has been added to card, Thank you!!")
        else:
            print("No such user found!! ")

    def view_balance(self):
        """Helps to show balance of user"""
        balance = self.user.view_balance()
        print(f"Your balance is -> {balance}.")

    def check_order(self):
        """checks if user has placed an order today"""
        response = self.user.check_order()
        if response is None:
            return False

        today = datetime.date.today()
        order_date = response[0].date()

        return today == order_date

    def give_feedback(self):
        """Checks
        1) if user has already given a feedback
        2) placed an order
        Then, gets criteria and submits user's feedback to add_feedback()"""
        feedback_already_given = self.user.check_user_feedback()
        if feedback_already_given:
            print("You have already given feedback, Thank You!")
            return

        placed_order = self.check_order()
        if not placed_order:
            print("You have to first place an order to give feedback !")
            return

        criterias = self.user.get_menu_fdb_criterias()
        if criterias is not None:
            feedback = []
            for criteria in criterias:
                current_cr = criteria["criteria"].title()
                rating = GetInput.get_ratings(
                    f"Please give ratings(out of 5) for the criteria [{current_cr}] -> "
                )
                review = input(
                    f"Please give reviews for the criteria [{current_cr}] - "
                )

                feedback.append(
                    (
                        self.user.user_id,
                        criteria["cr_id"],
                        criteria["menu_id"],
                        rating,
                        review,
                    )
                )
            self.user.add_feedback(feedback)
        else:
            print("No criterias have been decided for the current menu!! ")

    def check_rejected_menu(self):
        """checks if there are any rejected menus"""
        db = Database()
        response = db.get_item(queries.CHECK_REJECTED_MENU, (self.user.grp_id,))
        return response

    def check_menu_status(self, status):
        """checks menu status of any group"""
        db = Database()
        response = db.get_item(queries.CHECK_MENU_STATUS, (status, self.user.grp_id))
        return response

    def propose_menu(self):
        """gets input from admin and calls the propose_menu()"""
        menu_items = []
        while True:
            menu_item = GetInput.get_input(prompts.PROPOSE_MENU_TEXT)

            menu_items.append(menu_item)
            user_input = GetInput.get_input("Do you wish to add more items ??(y/n) ")
            if user_input == "n":
                break
        date = GetInput.get_date(
            "Please enter date for which the menu will be published(YYYY-MM-DD) "
        )
        self.user.propose_menu(menu_items, date)

    def set_fdb_criteria(self):
        """Checks if Feedback criterias are set for current menu
        and if not,
        takes input from admin, and calls set_fdb_criteria"""
        is_criteria_set = self.user.get_menu_fdb_criterias()
        if is_criteria_set is not None:
            print("Criterias are already decided for the current menu !! ")
            return
        criteria = self.user.get_fdb_criteria()

        print("\nCurrent list ->")
        self.user.display_criteria(criteria)
        new_criterias = criteria
        criterias_to_insert = []
        user_input = GetInput.get_yesno(
            "Do you wish to add another criteria to the criteria list? (y/n) "
        )

        while user_input == "y":
            new_criteria = GetInput.get_input(
                "\nPlease enter any new criteria you wish to get the feedback for - "
            )
            if new_criteria.lower() not in new_criterias:
                new_criterias.append(new_criteria.lower())
                criterias_to_insert.append(new_criteria.lower())
                user_input = GetInput.get_yesno(
                    "\nDo you wish to add another criteria? (y/n) "
                )
            else:
                print("Criteria already present!!! ")
                user_input = GetInput.get_yesno(
                    "Do you wish to add another criteria? (y/n) "
                )

        os.system("cls")
        print("\n\nUpdated list ")
        self.user.display_criteria(new_criterias)
        self.user.add_new_criteria(criterias_to_insert)

        criterias_selected = []
        while True:
            criteria_selected = GetInput.get_input(
                "Please enter the criteria you want to get feedback for - "
            )
            if criteria_selected.lower() not in new_criterias:
                print("Please enter valid criteria!! ")
                continue

            criterias_selected.append(criteria_selected.lower())
            user_input = GetInput.get_yesno(
                "Do you wish to get feedback on another criteria? (y/n) "
            )

            if user_input == "n":
                print("\nCriterias applied!! Thank you! \n")
                break

        self.user.set_fdb_criteria(criterias_selected)

    def view_all_fdb(self):
        """Helps to view all feedbacks on current menu"""
        feedbacks = self.user.view_all_feedbacks()
        if len(feedbacks) == 0:
            print("No feedbacks available!! ")
        else:
            feedback_dict = {}

            for feedback in feedbacks:
                if feedback_dict.get(feedback[0]) is None:
                    feedback_dict[feedback[0]] = []
                feedback_dict[feedback[0]].append([feedback[1], feedback[2]])
            first_key = list(feedback_dict.keys())[0]
            criteria_fdb_length = len(feedback_dict.get(first_key))
            for i in range(0, criteria_fdb_length):
                table = PrettyTable(["Criteria", "Ratings(out of 5)", "Comments"])
                table.title = f"Feedback {i+1}"
                for feedback in feedback_dict:
                    table.add_row(
                        [
                            f"{feedback}",
                            f"{feedback_dict[feedback][i][0]}",
                            f"{feedback_dict[feedback][i][1]}",
                        ]
                    )
                print(table)

    def view_filtered_fdb(self):
        """Helps to view feedbacks according to some filters on current menu"""
        response = self.user.view_all_feedbacks()
        feedback_dict = {}
        for feedback in response:
            if feedback_dict.get(feedback[0]) is None:
                feedback_dict[feedback[0]] = []
            feedback_dict[feedback[0]].append([feedback[1], feedback[2]])

        if len(feedback_dict) == 0:
            print("No feedbacks available!! ")
        else:
            print("Filters available -> ")
            table = PrettyTable(["S.no.", "Filter"])
            for index, criteria in enumerate(feedback_dict, start=1):
                table.add_row([f"{index}", f"{criteria}"])
            print(table)

            user_filter = GetInput.get_input(
                "Please enter the filter you want to apply - "
            )
            while user_filter.lower() not in feedback_dict:
                user_filter = input("Please enter a valid filter - ")

            table = PrettyTable(["Ratings (out of 5)", "Comments"])
            table.title = f"Criteria -> {user_filter.title()}"
            user_filter_1 = feedback_dict.get(user_filter.lower())
            for feedback in user_filter_1:
                table.add_row(
                    [
                        f"{feedback[0]}",
                        f"{feedback[1] if feedback[1] != '' else 'No comments'}",
                    ]
                )
            print(table)

    def view_fdb(self):
        """View for letting the admin choose how he wants to view the feedback"""
        print("1) View all feedbacks on current menu.")
        print("2) View feedbacks according to a criteria.")
        user_choice = input("Choose from the above options - ")
        while not user_choice in ("1", "2"):
            user_choice = input("Please choose between 1 and 2 - ")

        if user_choice == "1":
            self.view_all_fdb()
        else:
            self.view_filtered_fdb()

    def validate_user(self):
        """Validates the user"""
        user_id = GetInput.get_id("Please provide user id - ")

        is_validated = self.user.validate_user(int(user_id))
        if is_validated:
            print("User is validated!!!")
            user_choice = GetInput.get_yesno(
                "Do you want to place order for the employee(y/n) ? "
            )
            if user_choice == "y":
                self.receive_order(user_id=int(user_id))
        else:
            print("No such user found!!")

    def receive_order(self, user_id=None):
        """ "Checks if employee is validated, and then places the order"""
        if user_id is None:
            print("You need to validate employee before placing an order !")
            self.validate_user()
        else:
            balance = self.user.view_balance(user_id=user_id)
            if balance < 137:
                print("Low Balance, Contact admin or Topup Card!")
            else:
                self.user.update_balance(user_id=user_id, amount=-137)
                self.user.store_order(
                    user_id=user_id, amount=137, created_by=self.user.user_name
                )
                print("Order placed! Thank You!!")

    def accept_menu(self):
        """Helps the user to accept the pending menu"""
        menu = self.user.get_pending_menu()
        if len(menu) == 0:
            print("No menu available to accept currently. ")
        else:
            self.user.display_menu(menu)
            _menu_id = menu[0][2]
            user_choice = GetInput.get_yesno("Do you accept the menu?? (y/n) ")
            if user_choice == "y":
                self.user.accept_menu(_menu_id)
                print("Menu has been accepted, Thank You !!")
            else:
                comments = input("Please specify the reason - ")
                self.user.reject_menu(_menu_id, comments)

    def publish_menu(self):
        """Communicates with publish_menu()
        and helps to publish the menu"""
        items = self.user.get_not_published_menu()
        try:
            self.user.display_menu(items)
        except NoMenuFoundError:
            print("No menu available to publish currently. ")
        else:
            print("The above menu has been approved!!")
            _menu_id = items[0][2]
            _menu_date = items[0][1]

            user_choice = GetInput.get_yesno("Do you want to publish the menu?? (y/n) ")
            if user_choice == "y":
                self.user.publish_menu(_menu_id, _menu_date)
                os.system("cls")
                print("\n\nMenu has been added!! ")
                print(
                    "\nPlease decide the criterias on which\
                     you want to get feedbacks for the menu! "
                )
                self.set_fdb_criteria()
            else:
                print("The menu has been discarded! ")
                self.user.discard_menu((_menu_id,))


class GetInput:
    """
    class to group all input methods
    The associated methods also validate input
    """

    @staticmethod
    def get_user_name():
        """validates username according to regex = [A-Za-z0-9]+"""
        user_name = input("Enter username - ")
        if not Validators.validate_username(user_name):
            print("Invalid Username!! Try again!")
            user_name = GetInput.get_user_name()

        return user_name

    @staticmethod
    def get_password():
        """validates username according to regex ->
        ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"""

        password = input("Enter password - ")
        if not Validators.validate_password(password):
            print("Invalid password!! Try again!")
            password = GetInput.get_password()

        return password

    @staticmethod
    def get_yesno(message):
        """validates username according to  regex = [yn]"""
        user_choice = input(message)
        if not Validators.validate_yesno(user_choice):
            print("Invalid Choice, Please try again ")
            user_choice = GetInput.get_yesno(message)

        return user_choice

    @staticmethod
    def get_input(message):
        """validates input according to  regex = [A-Za-z0-9\s]+"""
        user_input = input(message)
        if not Validators.validate_input(user_input):
            print("Invalid input, Please try again!!")
            user_input = GetInput.get_input(message)

        return user_input

    @staticmethod
    def get_date(message):
        """validates date according to  regex = [0-9]{4}[-][0-9]{2}[-][0-9]{2}"""
        user_input = input(message)
        if not Validators.validate_date(user_input):
            print("Invalid date, Please try again!!")
            user_input = GetInput.get_date(message)

        return user_input

    @staticmethod
    def get_id(message):
        """validates date according to  regex = [0-9]+"""
        user_input = input(message)
        if not Validators.validate_id(user_input):
            print("Invalid id, Please try again!!")
            user_input = GetInput.get_id(message)

        return user_input

    @staticmethod
    def get_ratings(message):
        """validates ratings according to  regex = [1-5]"""
        user_input = input(message)
        if not Validators.validate_rating(user_input):
            print("Invalid Rating, Please try again!!")
            user_input = GetInput.get_ratings(message)

        return user_input


if __name__ == "__main__":
    print(GetInput.get_date("Enter date "))
