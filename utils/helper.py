from utils.validator import Validator
from configuration.default import Settings

class Helper(object):

    def __init__(self, data):
        self.data = data

    def validate_name(self):
        name = self.data[Settings.ADD_REQUEST_NAME_PARAM]
        name = name.strip()
        Validator.validate_length( \
                val = name, \
                param = Settings.ADD_REQUEST_NAME_PARAM, \
                expected = Settings.ADD_REQUEST_NAME_PARAM_LENGTH, \
            )
        Validator.validate_alphanumeric( \
                val = name,
                param = Settings.ADD_REQUEST_NAME_PARAM, \
            )
        return

    def validate_times(self):
        times = self.data[Settings.ADD_REQUEST_TIMES_PARAM]
        Validator.validate_list_type( \
                val = times,
                param = Settings.ADD_REQUEST_TIMES_PARAM, \
            )

    def validate_data(self):
        self.validate_name()
        self.validate_times()


    def validate_add_request(self):
        Validator.validate_for_missing_parameters(data = self.data, required_params = Settings.ADD_REQUEST_PARAMS_TYPE)
        Validator.validate_for_parameter_type(data = self.data, required_params = Settings.ADD_REQUEST_PARAMS_TYPE)
        self.validate_data()

    @staticmethod
    def add_train_data(data):
        pass
