from datetime import datetime
import bisect

class Utils(object):

    @staticmethod
    def convert_string_datetime(val):
        val = val.strip().upper()
        a =  datetime.strptime(val, '%I:%M %p')
        return a

    @staticmethod
    def convert_datetime_str(val):
        return datetime.strftime(val, '%I:%M %p')

    @staticmethod
    def fetch_index_gte(data_dict, data, search):
        # returns time more than the current time
        idx = bisect.bisect_right(data, search)
        # if search time exists in input consider it to meet the equals criteria
        return idx - 1 if data[idx-1] == search else idx
