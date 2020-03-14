from datetime import datetime, timedelta

class Curve:
    """Model Curve represents consumcion on specidic date an hour
    @param  date    datetime(2020, 01, 01, 0)
    @param  kwh     float(1.0)
    """
    def __init__(self, date, kwh):
        self.date = date
        self.kwh = kwh
    
    def dayOfWeek(self):
        return self.date.weekday()

