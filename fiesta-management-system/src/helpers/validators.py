import re


class Validators:
    @staticmethod
    def validations(context, validator):
        matches = re.findall(validator, context)
        return (len(matches) > 0) and matches[0] == context

    @staticmethod
    def validate_id(user_id):
        validator = "[0-9]+"
        if Validators.validations(context=user_id, validator=validator):
            return user_id
        else:
            user_id = input("Please enter valid id - ")
            return Validators.validate_id(user_id)

    @staticmethod
    def validate_username(user_name):
        validator = "[A-Za-z0-9]+"
        if Validators.validations(context=user_name, validator=validator):
            return user_name
        else:
            user_name = input("Please enter valid user name - ")
            return Validators.validate_username(user_name)

    @staticmethod
    def validate_password(password):
        validator = (
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        if Validators.validations(context=password, validator=validator):
            return password
        else:
            password = input("Please enter valid password - ")
            return Validators.validate_password(password)

    @staticmethod
    def validate_input(inp):
        validator = "[A-Za-z0-9\s]+"
        if Validators.validations(context=inp, validator=validator):
            return inp
        else:
            inp = input("Please enter valid input - ")
            return Validators.validate_input(inp)

    @staticmethod
    def validate_yesno(inp):
        validator = "[yn]"
        if Validators.validations(context=inp, validator=validator):
            return inp
        else:
            inp = input("Please choose between y/n - ")
            return Validators.validate_yesno(inp)

    @staticmethod
    def validate_rating(inp):
        validator = "[1-5]"
        if Validators.validations(context=inp, validator=validator):
            return inp
        else:
            inp = input("Please enter between [1-5] - ")
            return Validators.validate_rating(inp)


if __name__ == "__main__":
    print(Validators.validate_input())
