import re


class Validators:

    @staticmethod
    def validations(context, validator):
        matches = re.findall(validator, context)
        return (len(matches) > 0) and matches[0] == context

    @staticmethod
    def validate_email(email):
        validator = "[A-Za-z0-9]+@[a-z]+\.com"
        return Validators.validations(context=email, validator=validator)

    @staticmethod
    def validate_id(user_id):
        validator = "[0-9]+"
        return Validators.validations(context=user_id, validator=validator)

    @staticmethod
    def validate_name(user_name):
        validator = "[A-Za-z]+"
        return Validators.validations(context=user_name, validator=validator)

    @staticmethod
    def validate_department(department):
        validator = "[A-Za-z]+"
        return Validators.validations(context=department, validator=validator)


if __name__ == "__main__":
    print(Validators.validate_email("abc@gmailcom"))
    print(Validators.validate_email("abc@gmail.com   hello"))
    print(Validators.validate_id(1))
