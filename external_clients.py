# external_clients.py
import arrow

class User:
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        self.arrow_object = arrow.Arrow(year, month, day, hour, minute, second, microsecond, tzinfo)

    def get_arrow_object(self):
        return self.arrow_object
