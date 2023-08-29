import re


class Validators:
    @staticmethod
    def validations(context, validator):
        matches = re.findall(validator, context)
        return (len(matches) > 0) and matches[0] == context

    @staticmethod
    def validate_id(user_id):
        validator = "[0-9]+"
        return Validators.validations(context=user_id, validator=validator)

    @staticmethod
    def validate_username(user_name):
        validator = "[A-Za-z0-9]+"
        return Validators.validations(context=user_name, validator=validator)

    @staticmethod
    def validate_password(password):
        validator = (
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        return Validators.validations(context=password, validator=validator)

    @staticmethod
    def validate_input(inp):
        validator = "[A-Za-z0-9\s]+"
        return Validators.validations(context=inp, validator=validator)

    @staticmethod
    def validate_yesno(inp):
        validator = "[yn]"
        return Validators.validations(context=inp, validator=validator)

    @staticmethod
    def validate_rating(inp):
        validator = "[1-5]"
        return Validators.validations(context=inp, validator=validator)

    @staticmethod
    def validate_date(date):
        validator = "[0-9]{4}[-][0-9]{2}[-][0-9]{2}"
        return Validators.validations(context=date, validator=validator)
