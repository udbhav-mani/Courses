import re
import jsonschema


class Validators:
    @staticmethod
    def validations(context, validator):
        matches = re.findall(validator, context)
        return (len(matches) > 0) and matches[0] == context

    @staticmethod
    def validate_request(schema, data):
        try:
            jsonschema.validate(instance=data, schema=schema)
        except TypeError as error:
            return str(error)
