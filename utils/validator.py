from datetime import datetime

from utils.exceptions import *
from configuration.default import Settings

class Validator(object):

    @staticmethod
    def validate_string_type(val, param = None):
        if not isinstance(val, str):
            raise TypeError(expected = str(str), param = param)
        return

    @staticmethod
    def validate_int_type(val, param = None):
        if not isinstance(val, int):
            raise TypeError(expected = str(int), param = param)
        return

    @staticmethod
    def validate_dict_type(val, param = None):
        if not isinstance(val, dict):
            raise TypeError(expected = str(dict), param = param)
        return

    @staticmethod
    def validate_list_type(val, param = None):
        if not isinstance(val, list):
            raise TypeError(expected = str(list), param = param)
        return


    @staticmethod
    def validate_for_parameter_type(data, required_params):
        # TODO: Add tests!
        Validator.validate_dict_type(data)
        Validator.validate_dict_type(required_params)

        invalid_type = []
        for key, val in required_params.items():
            if not isinstance(key, val):
                invalid_type.append(f"'{key}' of type: {val}")
        if invalid_type:
            raise InvalidTypeArguments(invalid_type = invalid_type)
        return

    @staticmethod
    def validate_for_missing_parameters(data, required_params):
        Validator.validate_dict_type(data)
        Validator.validate_dict_type(required_params)

        missing = []
        for key in required_params:
            if data.get(key, None) is None:
                missing.append(key)
        if missing:
            raise ExpectedArguments(expected = required_params, missing = missing)
        return

    @staticmethod
    def validate_length(val, param, expected):
        Validator.validate_string_type(val)
        Validator.validate_string_type(param)
        Validator.validate_int_type(expected)

        if len(val) != expected:
            raise UnExpectedParamLength(param, expected, actual = len(val))
        return

    @staticmethod
    def validate_alphanumeric(val, param):
        Validator.validate_string_type(val)
        Validator.validate_string_type(param)

        if not val.isalnum():
            raise TypeError(expected = str(str.isalnum), param = param)
        return

    @staticmethod
    def validate_time(val):
        Validator.validate_string_type(val)
        val = val.strip().upper()
        try:
            datetime.strptime(val, '%I:%M %p')
        except Exception as e:
            raise e
