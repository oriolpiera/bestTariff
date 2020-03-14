from datetime import datetime, timedelta
import numpy as np

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
    @param  start_hour      int from 0 to 22
    @param  end_hour        int from 1 to 23
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

class Tariff:
    """Model Tariff represents all tariff of the contract
    @param  periods     matrix that represent a whole week of prices
    """
    def __init__(self, periods=None):
        if periods is None:
            periods = np.zeros(shape=(7,24))
        self.periods = periods

    def loadTariffPeriod(self, tariffPeriodList):
        """Load TariffPeriod to Tariff matrix {periods}
        Arguments:
            tariffPeriodList {[TariffPeriod]} -- List of TariffPeriod objects
        """
        for tariffPeriod in tariffPeriodList:
            hour = tariffPeriod.start_hour
            while hour <= tariffPeriod.end_hour:
                if self.periods[tariffPeriod.day_of_week][hour] != 0:
                    raise Exception("Overlap tariff period")
                self.periods[tariffPeriod.day_of_week][hour] \
                    = tariffPeriod.kwh_price
                hour += 1

    def getMatrix(self):
        return self.periods

    def isCompleted(self):
        return 0 not in self.periods
