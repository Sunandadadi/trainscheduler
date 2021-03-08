from unittest import TestCase
from utils.helper import Helper
from configuration.default import Settings

class TestAddRequest(TestCase):

    def test_empty_name_for_validate_name(self):
        data = {Settings.REQUEST_NAME_PARAM: ''}
        a = Helper()
        try:
            a.validate_name(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Parameter: 'name' of length: 4, recieved: 0")

    def test_incorrect_length_for_validate_name(self):
        data = {Settings.REQUEST_NAME_PARAM: '1234sd'}
        a = Helper()
        try:
            a.validate_name(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Parameter: 'name' of length: 4, recieved: 6")

    def test_not_alphanum_name_for_validate_name(self):
        data = {Settings.REQUEST_NAME_PARAM: '#$@!'}
        a = Helper()
        try:
            a.validate_name(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected Parameter: 'name' of type: <method 'isalnum' of 'str' objects>")

    def test_empty_validate_times_list(self):
        data = {Settings.REQUEST_TIME_PARAM: []}
        a = Helper()
        try:
            ret = a.validate_times_list(data)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "Expected not empty value for time but recieved []")
