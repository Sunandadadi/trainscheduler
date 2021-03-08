from utils.validator import Validator
from configuration.default import Settings
from modules.train_line import TrainLine

class Helper(object):

    def __init__(self, data=None):
        self.data = data

    def validate_name(self, item):
        name = item.get(Settings.REQUEST_NAME_PARAM)
        name = name.strip()
        Validator.validate_length( \
                val = name, \
                param = Settings.REQUEST_NAME_PARAM, \
                expected = Settings.ADD_REQUEST_NAME_PARAM_LENGTH, \
            )
        Validator.validate_alphanumeric( \
                val = name,
                param = Settings.REQUEST_NAME_PARAM, \
            )
        return

    def validate_times_list(self, item):
        times = item.get(Settings.REQUEST_TIME_PARAM)
        Validator.validate_list_type( \
                val = times,
                param = Settings.REQUEST_TIME_PARAM, \
            )
        Validator.validate_times(times)
        return


    def validate_data(self):
        list(map(lambda item: self.validate_name(item), self.data))
        list(map(lambda item: self.validate_times_list(item), self.data))
        return

    def validate_add_request(self):
        Validator.validate_for_missing_parameters(data = self.data, required_params = Settings.ADD_REQUEST_PARAMS_TYPE)
        Validator.validate_for_parameter_type(data = self.data, required_params = Settings.ADD_REQUEST_PARAMS_TYPE)
        self.validate_data()
        return

    def add_train_data(self):
        self.validate_add_request()
        list(map(lambda item: TrainLine.save_train_line(item), self.data))
        return

    def validate_fetch_request(self):
        Validator.validate_for_missing_parameters(data = [self.data], required_params = Settings.FETCH_REQUEST_PARAMS_TYPE)
        Validator.validate_for_parameter_type(data = [self.data], required_params = Settings.FETCH_REQUEST_PARAMS_TYPE)
        time = self.data[Settings.REQUEST_TIME_PARAM]
        Validator.validate_time(time)
        return

    def fetch_simultaneous_trains(self):
        self.validate_fetch_request()
        return TrainLine.fetch_simultaneous_train_arrivals(self.data)
