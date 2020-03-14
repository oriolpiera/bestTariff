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

class TariffPeriod:
    """Model TariffPeriod represents a tariff period on specific time and price
    @param  start_hour      int from 0 to 23
    @param  end_hour        int from 1 to 24
    @param  day_of_week     int from 0 to 6
    @param  kwh_price       float(1.0)
    """
    def __init__(self, start_hour, end_hour, day_of_week, kwh_price):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.day_of_week = day_of_week
        self.kwh_price = kwh_price
    
    def getPrice(self):
        return self.kwh_price