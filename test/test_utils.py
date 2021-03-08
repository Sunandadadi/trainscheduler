from unittest import TestCase
from datetime import datetime

from utils.utils import Utils

class TestAddRequest(TestCase):

    def test_nonetype_convert_string_datetime(self):
        val = None
        try:
            Utils.convert_string_datetime(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "'NoneType' object has no attribute 'strip'")

    def test_empty_for_convert_string_datetime(self):
        val = ''
        try:
            Utils.convert_string_datetime(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "time data '' does not match format '%I:%M %p'")

    def test_invalid_for_convert_string_datetime(self):
        val = '2: 34 PM'
        try:
            Utils.convert_string_datetime(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "time data '2: 34 PM' does not match format '%I:%M %p'")

    def test_valid_convert_string_datetime(self):
        val = '2:34 PM'
        ret = Utils.convert_string_datetime(val)
        self.assertEqual(ret, datetime.strptime(val, '%I:%M %p'))

    def test_for_convert_string_datetime(self):
        val = '02:34 PM'
        ret = Utils.convert_string_datetime(val)
        self.assertEqual(ret, datetime.strptime(val, '%I:%M %p'))

    def test_nonetype_convert_datetime_str(self):
        val = None
        try:
            Utils.convert_datetime_str(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'NoneType' object")

    def test_empty_for_convert_datetime_str(self):
        val = ''
        try:
            Utils.convert_datetime_str(val)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'str' object")

    def test_invalid_for_convert_datetime_str(self):
        time = '2: 34 PM'
        val = datetime.strptime(time, '%I: %M %p')
        ret = Utils.convert_datetime_str(val)
        self.assertNotEqual(ret, time)

    def test_for_convert_datetime_str(self):
        time = '2:34 PM'
        expected_time = '02: 34 PM'
        val = datetime.strptime(time, '%I:%M %p')
        ret = Utils.convert_datetime_str(val)
        self.assertNotEqual(ret, time)
        self.assertNotEqual(ret, expected_time)

    def test_valid_for_convert_datetime_str(self):
        time = '02:34 PM'
        val = datetime.strptime(time, '%I:%M %p')
        ret = Utils.convert_datetime_str(val)
        self.assertEqual(ret, time)

    def test_nonetype_fetch_index_gte(self):
        data_dict, data, search = None, None, None
        try:
            Utils.fetch_index_gte(data_dict, data, search)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "object of type 'NoneType' has no len()")

    def test_empty_fetch_index_gte(self):
        data_dict, data, search = {}, [], 1
        try:
            Utils.fetch_index_gte(data_dict, data, search)
            self.assertFail()
        except Exception as err:
            self.assertEqual(str(err), "list index out of range")

    def test_valid_fetch_index_gte(self):
        data_dict = {1: 1, 2: 2, 3: 3}
        data, search = list(data_dict.keys()), 2
        ret = Utils.fetch_index_gte(data_dict, data, search)
        self.assertEqual(ret, data.index(2))

    def test_valid_fetch_index_gte(self):
        data_dict = {1: 1, 2: 2, 3: 3}
        data, search = list(data_dict.keys()), 4
        ret = Utils.fetch_index_gte(data_dict, data, search)
        self.assertEqual(ret, len(data_dict))

    def test_valid_fetch_index_gte(self):
        data_dict = {1: 1, 2: 2, 3: 3}
        data, search = list(data_dict.keys()), 0
        ret = Utils.fetch_index_gte(data_dict, data, search)
        self.assertEqual(ret, 0)
