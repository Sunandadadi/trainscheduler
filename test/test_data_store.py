from unittest import TestCase
from sortedcontainers import SortedDict

from utils.utils import Utils
from modules.data_store import DataStore
from configuration.default import Settings

class TestAddRequest(TestCase):

    @classmethod
    def setup_class(cls):
        cls.store = DataStore()

    def test_datastore_initailization(self):
        self.assertEqual(SortedDict, type(self.store.datastore))

    def test_set_datastore(self):
        a = {'name': 'ed21', 'time': '10:00 AM'}
        b = {'name': 'ed21', 'time': '11:00 PM'}
        a_time = Utils.convert_string_datetime(a['time'])
        b_time = Utils.convert_string_datetime(b['time'])
        self.store.set(a_time, a['name'])
        self.store.set(b_time, b['name'])
        self.assertEqual(self.store.datastore, self.store.keys())

    def test_fetch_datastore(self):
        a = {'name': 'ed21', 'time': '10:00 AM'}
        time = Utils.convert_string_datetime(a['time'])
        self.store.set(time, a['name'])
        actual = self.store.fetch(time)
        self.assertEqual(actual, self.store.datastore[time])

    def test_fetch_empty_datastore(self):
        time = '03:00 PM'
        actual = self.store.fetch(time)
        self.assertEqual(actual, set())
