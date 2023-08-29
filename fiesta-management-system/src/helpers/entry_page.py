import datetime
import maskpass
from prettytable import PrettyTable
from src.controllers.login import Login
from src.controllers.user import User
from src.helpers.exceptions import NoSuchUserError, NoMenuFoundError
from src.helpers.validators import Validators
from src.models.database import Database
from src.utils import prompts, queries


class ChoiceDisplayer:
    def __init__(self, user=None):
        self.user = user

    def login_view(self):
        user_name = input("Enter username - ")
        user_name = Validators.validate_username(user_name)

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
                self.display_choices()
            else:
                print("Login Failed!! Please input valid credentials!!")

    def check_rejected_menu(self):
        db = Database()
        response = db.get_item(queries.CHECK_REJECTED_MENU, (self.user.grp_id,))
        return response

    def check_menu_status(self, status):
        db = Database()
        response = db.get_item(queries.CHECK_MENU_STATUS, (status, self.user.grp_id))
        return response

    def propose_menu(self):
        menu_items = list()
        while True:
            menu_item = input(prompts.PROPOSE_MENU_TEXT)
            menu_item = Validators.validate_input(menu_item)

            menu_items.append(menu_item)
            user_input = input("Do you wish to add more items ??(y/n) ")
            user_input = Validators.validate_yesno(user_input)

            if user_input == "n":
                break
        date = input(
            "Please enter date for which the menu will be published(YYYY-MM-DD) "
        )
        self.user.propose_menu(menu_items, date)

    def set_fdb_criteria(self):
        is_criteria_set = self.user.get_menu_fdb_criterias()
        if is_criteria_set is not None:
            print("Criterias are already decided for the current menu !! ")
            return
        criteria = self.user.get_fdb_criteria()
        print("Current list ->")
        self.user.display_criteria(criteria)
        new_criterias = criteria
        criterias_to_insert = list()
        user_input = input(
            "Do you wish to add another criteria to the criteria list? (y/n) "
        )
        user_input = Validators.validate_yesno(user_input)

        while user_input == "y":
            new_criteria = input(
                "Please enter any new criteria you wish to get the feedback for - "
            )
            new_criteria = Validators.validate_input(new_criteria)
            if new_criteria.lower() not in new_criterias:
                new_criterias.append(new_criteria.lower())
                criterias_to_insert.append(new_criteria.lower())
                user_input = input("Do you wish to add another criteria? (y/n) ")
                user_input = Validators.validate_yesno(user_input)
            else:
                print("Criteria already present!!! ")
                user_input = input("Do you wish to add another criteria? (y/n) ")
                user_input = Validators.validate_yesno(user_input)

        print("Updated list ")
        self.user.display_criteria(new_criterias)
        self.user.add_new_criteria(criterias_to_insert)

        criterias_selected = list()
        while True:
            criteria_selected = input(
                "Please enter the criteria you want to get feedback for - "
            )
            if criteria_selected.lower() not in new_criterias:
                print("Please enter valid criteria!! ")
                continue

            criterias_selected.append(criteria_selected.lower())
            user_input = input(
                "Do you wish to get feedback on another criteria? (y/n) "
            )
            user_input = Validators.validate_yesno(user_input)

            if user_input == "n":
                print("Criterias applied!! Thank you! ")
                break

        self.user.set_fdb_criteria(criterias_selected)

    def view_fdb(self):
        print("1) View all feedbacks on current menu.")
        print("2) View feedbacks according to a criteria.")
        user_choice = input("Choose from the above options - ")
        while not (user_choice == "1" or user_choice == "2"):
            user_choice = input("Please choose between 1 and 2 - ")

        if user_choice == "1":
            feedbacks = self.user.view_all_feedbacks()
            if len(feedbacks) == 0:
                print("No feedbacks available!! ")
            else:
                feedback_dict = dict()
                for feedback in feedbacks:
                    if feedback_dict.get(feedback[0]) is None:
                        feedback_dict[feedback[0]] = list()
                    feedback_dict[feedback[0]].append([feedback[1], feedback[2]])

                for feedback in feedback_dict:
                    print(f"{feedback} -> {feedback_dict[feedback]}")
        else:
            response = self.user.view_all_feedbacks()
            feedback_dict = dict()
            for feedback in response:
                if feedback_dict.get(feedback[0]) is None:
                    feedback_dict[feedback[0]] = list()
                feedback_dict[feedback[0]].append([feedback[1], feedback[2]])

            if len(feedback_dict) == 0:
                print("No feedbacks available!! ")
            else:
                print("Filters available -> ")
                t = PrettyTable(["S.no.", "Filter"])
                for index, filter in enumerate(feedback_dict, start=1):
                    t.add_row([f"{index}", f"{filter}"])
                print(t)

                user_filter = input("Please enter the filter you want to apply - ")
                while user_filter.lower() not in feedback_dict:
                    user_filter = input("Please enter a valid filter - ")

                print(f"Criteria -> {user_filter.title()}")
                t = PrettyTable(["Ratings (out of 5)", "Comments"])
                user_filter_1 = feedback_dict[user_filter]
                for feedback in user_filter_1:
                    t.add_row(
                        [
                            f"{feedback[0]}",
                            f"{feedback[1] if feedback[1] != '' else 'No comments'}",
                        ]
                    )
                print(t)

    def validate_user(self):
        user_id = input("Please provide user id - ")
        user_id = Validators.validate_id(user_id)

        is_validated = self.user.validate_user(int(user_id))
        if is_validated:
            print("User is validated!!!")
            user_choice = input("Do you want to place order for the employee(y/n) ? ")
            user_choice = Validators.validate_yesno(user_choice)

            if user_choice == "y":
                self.receive_order(user_id=int(user_id))
        else:
            print("No such user found!!")

    def receive_order(self, user_id=None):
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
        menu = self.user.get_pending_menu()
        if len(menu) == 0:
            print("No menu available to accept currently. ")
        else:
            self.user.display_menu(menu)
            _menu_id = menu[0][2]
            user_choice = input("Do you accept the menu?? (y/n) ")
            user_choice = Validators.validate_yesno(user_choice)
            if user_choice == "y":
                self.user.accept_menu(_menu_id)
                print("Menu has been accepted, Thank You !!")
            else:
                comments = input("Please specify the reason - ")
                self.user.reject_menu(_menu_id, comments)

    def publish_menu(self):
        items = self.user.get_npublished_menu()
        try:
            self.user.display_menu(items)
        except NoMenuFoundError:
            print("No menu available to publish currently. ")
        else:
            print("The above menu has been approved!!")
            _menu_id = items[0][2]
            _menu_date = items[0][1]

            user_choice = input("Do you want to publish the menu?? (y/n) ")
            user_choice = Validators.validate_yesno(user_choice)
            if user_choice == "y":
                self.user.publish_menu(_menu_id, _menu_date)
                print("\n\nMenu has been added!! ")
                print(
                    "\nPlease decide the criterias on which you want to get feedbacks for the menu! "
                )
                self.set_fdb_criteria()

    def admin_view(self):
        is_not_published = self.user.check_menu_status("not published")
        if is_not_published:
            print("\n\n!!! Your menu has been accepted, Please publish it!!!")

        is_rejected_response = self.check_rejected_menu()
        if is_rejected_response is not None:
            _menu_id = is_rejected_response[0]
            comments = is_rejected_response[1]
            print(
                f"\n\n\nYour Menu has been rejected, Please propose another menu!"
                f"\nReason - {comments if comments != '' else 'No comments'}"
            )

            print(prompts.UPDATE_MENU_TEXT)
            user_choice = input("Enter choice - ")
            if user_choice == "1":
                self.user.discard_menu(_menu_id)
                print("Menu has been discarded! ")
            elif user_choice == "2":
                print("Current Menu - ")
                response = self.user.view_menu(_menu_id)
                items_dict = dict()
                for index, tup in enumerate(response, start=1):
                    items_dict[index] = tup[0]

                item_number = int(input("Enter the item number you want to change - "))
                new_item = input("Enter the new item name - ")
                new_item = Validators.validate_input(new_item)

                self.user.update_menu(_menu_id, items_dict[item_number], new_item)

        while True:
            print(prompts.ADMIN_CHOICES)
            user_choice = self.get_choice()
            if user_choice == 1:
                self.propose_menu()
            elif user_choice == 2:
                self.publish_menu()
            elif user_choice == 3:
                self.set_fdb_criteria()
            elif user_choice == 4:
                self.view_fdb()
            else:
                self.user.view_accepted_menu()

            user_choice = input("\nDo you wish to continue?(y/n) - ")
            user_choice = Validators.validate_yesno(user_choice)

            if user_choice == "n":
                break

    def f_emp_view(self):
        is_pending = self.user.check_menu_status("pending")
        if is_pending:
            print("\n\n!!! There are pending menus!! Please review!!!")

        while True:
            print(prompts.F_EMP_CHOICES)
            user_choice = self.get_choice()
            if user_choice == 1:
                self.validate_user()
            elif user_choice == 2:
                self.receive_order()
            elif user_choice == 3:
                self.accept_menu()
            elif user_choice == 4:
                self.user.view_accepted_menu()
            else:
                self.topup_card()

            user_choice = input("\nDo you wish to continue?(y/n) - ")
            user_choice = Validators.validate_yesno(user_choice)

            if user_choice == "n":
                break

    def emp_view(self):
        print(prompts.HEADER)
        while True:
            print(prompts.EMP_CHOICES)
            user_choice = self.get_choice()
            if user_choice == 1:
                self.user.view_accepted_menu()
            elif user_choice == 2:
                self.user.place_order()
            elif user_choice == 3:
                self.view_balance()
            else:
                self.give_feedback()

            user_choice = input("\nDo you wish to continue?(y/n) - ")
            user_choice = Validators.validate_yesno(user_choice)

            if user_choice == "n":
                break

    def check_role(self):
        return self.user.role

    def choose_for_admin(self):
        user_input = input(prompts.VIEW_ADMIN_MENU)
        while not (user_input != "1" or user_input != "2"):
            user_input = input("\n\nPlease choose between 1 or 2 - ")
        if user_input == "1":
            self.admin_view()
        elif user_input == "2":
            self.emp_view()
        else:
            print("Please choose between 1 or 2 - ")
            self.choose_for_admin()

    def display_choices(self):
        if self.check_role() == "admin":
            self.choose_for_admin()
        elif self.check_role() == "f_emp":
            self.f_emp_view()
        else:
            self.emp_view()

    def entry(self):
        print("Welcome to Fiesta Management system.")
        self.login_view()

    def topup_card(self):
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
        balance = self.user.view_balance()
        print(f"Your balance is -> {balance}.")

    def check_order(self):
        response = self.user.check_order()
        if response is None:
            return False
        else:
            today = datetime.date.today()
            order_date = response[0].date()

            return today == order_date

    def give_feedback(self):
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
            feedback = list()
            for criteria in criterias:
                current_cr = criteria["criteria"].title()
                rating = input(
                    f"Please give ratings(out of 5) for the criteria [{current_cr}] -> "
                )
                while not Validators.validate_rating(rating):
                    rating = input("Please rate out of 5 -")
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

    @staticmethod
    def get_choice():
        user_choice = int(input("Enter choice - "))
        while user_choice not in range(1, 6):
            user_choice = int(input(f"Please choose between (1-5) - "))
        return user_choice


if __name__ == "__main__":
    obj = ChoiceDisplayer()
    obj.login_view()
