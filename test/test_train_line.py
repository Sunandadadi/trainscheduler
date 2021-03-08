from unittest import TestCase
from datetime import datetime
from sortedcontainers import SortedDict

from modules.train_line import TrainLine
from modules.data_store import DataStore
from configuration.default import Settings

class TestAddRequest(TestCase):

    def setUp(self):
        Settings.DATA_STORE = DataStore()

    def tearDown(self):
        Settings.DATA_STORE = None

    def test_save_train_line_for_single_entry(self):
        data = {
            "name": "a1de",
            "time": ["10:31 AM", "10:31 PM", "09:31 AM"]
        }
        TrainLine.save_train_line(data)
        expected = SortedDict({
            datetime(1900, 1, 1, 9, 31): [1, {'a1de'}],
            datetime(1900, 1, 1, 10, 31): [1, {'a1de'}],
            datetime(1900, 1, 1, 22, 31): [1, {'a1de'}]
            })
        self.assertEqual(Settings.DATA_STORE.keys(), expected)

    def test_save_train_line_for_multiple_entries(self):
        data1 = {
            "name": "a1de",
            "time": ["10:31 AM", "10:31 PM", "09:31 AM"]
        }
        data2 = {
            "name": "se23",
            "time": ["10:45 AM", "10:31 PM", "03:31 AM"]
        }
        TrainLine.save_train_line(data1)
        TrainLine.save_train_line(data2)
        expected = SortedDict({
            datetime(1900, 1, 1, 3, 31): [1, {'se23'}],
            datetime(1900, 1, 1, 9, 31): [1, {'a1de'}],
            datetime(1900, 1, 1, 10, 31): [1, {'a1de'}],
            datetime(1900, 1, 1, 10, 45): [1, {'se23'}],
            datetime(1900, 1, 1, 22, 31): [2, {'se23', 'a1de'}]
            })
        self.assertEqual(Settings.DATA_STORE.keys(), expected)

    def test_fetch_simultaneous_train_arrivals_for_empty_store(self):
        data = {
            "time": ["10:00 AM"]
        }
        ret = TrainLine.fetch_simultaneous_train_arrivals(data)
        self.assertEqual(ret, -1)

    def test_fetch_simultaneous_train_arrivals(self):
        data1 = {
            "name": "sd32",
            "time": ["10:31 AM", "10:31 PM", "09:31 AM"]
        }
        data2 = {
            "name": "df34",
            "time": ["10:45 AM", "10:31 PM", "03:31 AM"]
        }
        data = {
            "time": "10:00 AM"
        }
        TrainLine.save_train_line(data1)
        TrainLine.save_train_line(data2)
        ret = TrainLine.fetch_simultaneous_train_arrivals(data)
        self.assertEqual(ret, "10:31 PM")
