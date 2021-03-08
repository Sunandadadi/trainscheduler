from sortedcontainers import SortedDict

class DataStore(object):
    def __init__(self):
        self.datastore = SortedDict()

    def set(self, time, name):
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
        return self.datastore.get(time, set())

    def keys(self):
        return self.datastore
