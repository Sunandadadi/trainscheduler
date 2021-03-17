from sortedcontainers import SortedDict
import threading

class DataStore(object):
    def __init__(self):
        self.datastore = SortedDict()
        self.APP_LOCK = threading.Lock()

    def set(self, time, name):
        with self.APP_LOCK:
            if self.datastore.get(time, None) is None:
                # store is dictionary where key is the time and value is a list.
                # The list has two objects. Second ele is a set that stores the train line names
                # Fist ele stores a count of total elements in the set
                self.datastore[time] = [0, set()]

            if name not in self.datastore[time]:
                self.datastore[time][0] += 1
            self.datastore[time][1].add(name)
            return

    def fetch(self, time):
        with self.APP_LOCK:
            return self.datastore.get(time, set())

    def keys(self):
        return self.datastore
