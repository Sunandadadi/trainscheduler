from unittest import TestCase
from utils.validator import Validator

class TestAddRequest(TestCase):

    def test_invalid_validate_string_type(self):
        data = None
        try:
            Validator.validate_string_type(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_valid_validate_string_type(self):
        data = ''
        ret = Validator.validate_string_type(data)
        self.assertEqual(ret, None)

    def test_invalid_validate_int_type(self):
        data = ''
        try:
            Validator.validate_int_type(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'int'>")

    def test_valid_validate_int_type(self):
        data = 1
        ret = Validator.validate_int_type(data)
        self.assertEqual(ret, None)

    def test_invalid_validate_dict_type(self):
        data = []
        try:
            Validator.validate_dict_type(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'dict'>")

    def test_valid_validate_dict_type(self):
        data = {}
        ret = Validator.validate_dict_type(data)
        self.assertEqual(ret, None)

    def test_invalid_validate_list_type(self):
        data = None
        try:
            Validator.validate_list_type(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'list'>")

    def test_valid_validate_list_type(self):
        data = []
        ret = Validator.validate_list_type(data)
        self.assertEqual(ret, None)

    def test_invalid_data_for_validate_for_missing_parameters(self):
        data = None
        required_params = {}
        try:
            Validator.validate_for_missing_parameters(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'list'>")

    def test_invalid_required_params_for_validate_for_missing_parameters(self):
        data = []
        required_params = None
        try:
            Validator.validate_for_missing_parameters(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'dict'>")

    def test_missing_data_for_validate_for_missing_parameters(self):
        data = [{
            'param1': 'something'
        }]
        required_params = {
            'param1': str,
            'param2': str
        }
        try:
            Validator.validate_for_missing_parameters(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), 'Expected param1, param2 as arguments. Missing keys: param2')

    def test_valid_input_for_validate_for_missing_parameters(self):
        data = [{
            'param1': 'testing'
        }]
        required_params = {
            'param1': str
        }
        ret = Validator.validate_for_missing_parameters(data, required_params)
        self.assertEqual(ret, None)

    def test_nonetype_for_val_in_validate_length(self):
        val, param, expected = None, None, None
        try:
            Validator.validate_length(val, param, expected)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_nonetype_for_param_in_validate_length(self):
        val, param, expected = '123', None, None
        try:
            Validator.validate_length(val, param, expected)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_nonetype_for_param_in_validate_length(self):
        val, param, expected = '123', None, None
        try:
            Validator.validate_length(val, param, expected)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_nonetype_for_expected_in_validate_length(self):
        val, param, expected = '123', 'test', None
        try:
            Validator.validate_length(val, param, expected)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'int'>")

    def test_incorrect_length_in_validate_length(self):
        val, param, expected = '123', 'test', 4
        try:
            Validator.validate_length(val, param, expected)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Parameter: 'test' of length: 4, recieved: 3")

    def test_correct_length_in_validate_length(self):
        val, param, expected = '123', 'test', 3
        ret = Validator.validate_length(val, param, expected)
        self.assertEqual(ret, None)

    def test_nonetype_for_val_in_validate_alphanum(self):
        val, param = None, 'test'
        try:
            Validator.validate_alphanumeric(val, param)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_nonetype_for_param_in_validate_alphanum(self):
        val, param = 'test', None
        try:
            Validator.validate_alphanumeric(val, param)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'str'>")

    def test_invalid_string_in_validate_alphanum(self):
        val, param = '% $ ', 'test'
        try:
            Validator.validate_alphanumeric(val, param)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Parameter: 'test' of type: <method 'isalnum' of 'str' objects>")

    def test_valid_string_in_validate_alphanum(self):
        val, param = 't12s', 'test'
        ret = Validator.validate_alphanumeric(val, param)
        self.assertEqual(ret, None)

    def test_nonetype_for_data_in_validate_for_parameter_type(self):
        data, required_params = None, {}
        try:
            Validator.validate_for_parameter_type(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'list'>")

    def test_nonetype_for_params_in_validate_for_parameter_type(self):
        data, required_params = [], None
        try:
            Validator.validate_for_parameter_type(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Type: <class 'dict'>")

    def test_invalid_for_validate_for_parameter_type(self):
        data = [
            {'param1': 'test'},
            {'param1': 1}
        ]
        required_params = {
            'param1': str
        }
        try:
            Validator.validate_for_parameter_type(data, required_params)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "TypeError: Expected paramerter 'param1' of type: <class 'str'>")

    def test_invalid_for_validate_for_parameter_type(self):
        data = [
            {'param1': 'test1'},
            {'param1': 'test2'}
        ]
        required_params = {
            'param1': str
        }
        ret = Validator.validate_for_parameter_type(data, required_params)
        self.assertEqual(ret, None)

    def test_nonetype_in_validate_time(self):
        val = None
        try:
            Validator.validate_time(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected not empty value for time but recieved None")

    def test_invalid_str_in_validate_time(self):
        val = '12:00PM'
        try:
            Validator.validate_time(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "time data '12:00PM' does not match format '%I:%M %p'")

    def test_invalid_str_in_validate_time(self):
        val = '12:00 PM'
        ret = Validator.validate_time(val)
        self.assertEqual(ret, None)
