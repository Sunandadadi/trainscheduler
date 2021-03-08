import logging

from modules.data_store import DataStore
from utils.exceptions import *

class Settings(object):
    logging.basicConfig(level=logging.DEBUG, filename='train_scheduler.log', format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)
    WELCOME_TEXT = 'Welcome!'
    ADD_SUCCESS_TEXT = 'The data is successfully stored!'
    REQUEST_NAME_PARAM = 'name'
    REQUEST_TIME_PARAM = 'time'
    ADD_REQUEST_PARAMS_TYPE = {
            REQUEST_NAME_PARAM: str,
            REQUEST_TIME_PARAM: list
        }
    FETCH_REQUEST_PARAMS_TYPE = {
            REQUEST_TIME_PARAM: str
        }
    ADD_REQUEST_NAME_PARAM_LENGTH = 4
    SIMULTANEOUS_TRAIN_COUNT_THRESHOLD = 2
    DATA_STORE = DataStore()
    DEFINED_EXCEPTIONS = (ExpectedArguments, InvalidTypeArguments, UnExpectedParamLength, TypeError)
