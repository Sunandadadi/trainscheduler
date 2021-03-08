from configuration.default import Settings
from utils.utils import Utils

class TrainLine(object):

    @staticmethod
    def save_train_line(data):
        name = data['name']
        # Converting to datetime to accomodate for changes in input format or handling multiple formats
        list(map(lambda time: Settings.DATA_STORE.set(Utils.convert_string_datetime(time), name), \
                data[Settings.REQUEST_TIME_PARAM])
            )
        Settings.logger.info(f'Updated datastore: {Settings.DATA_STORE.keys()}')
        return

    @staticmethod
    def fetch_simultaneous_train_arrivals(data):
        store = Settings.DATA_STORE.keys()
        if not store:
            return -1

        search_time = Utils.convert_string_datetime(data['time'])
        store_times = store.keys()
        idx = Utils.fetch_index_gte(store, store_times, search_time)

        if idx == len(store_times):
            return TrainLine.fetch_time(store_times, search_time, idx = 0)
        return TrainLine.fetch_time(store_times, search_time, idx = idx)

    @staticmethod
    def fetch_time(store_times, search_time, idx):
        store = Settings.DATA_STORE.keys()
        for time in range(idx, len(store_times)):
            if store[store_times[time]][0] >= Settings.SIMULTANEOUS_TRAIN_COUNT_THRESHOLD:
                return Utils.convert_datetime_str(store_times[time])
        return -1
