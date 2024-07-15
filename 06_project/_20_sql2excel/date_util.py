import datetime


class datetime_util(object):

    def __init__(self):
    @staticmethod
    def datetime2string(a_datetime: datetime.datetime, format_pattern: str) -> str:
        return a_datetime.strftime(format_pattern)

    @staticmethod
    def string2datetime(a_string: str, format_patten: str) -> datetime.datetime:
        return datetime.datetime.strptime(a_string, format_patten)

    @staticmethod
    def datetime_plus_days(a_datetime: datetime.datetime, day_cnt: int) -> datetime.datetime:
        return a_datetime + datetime.timedelta(days=day_cnt)

