from datetime import datetime, timedelta
import numpy as np
import calendar

#TARIFF TYPES
TARIFF_TYPE_ENERGY = 1
TARIFF_TYPE_POWER = 2

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

class Tariff:
    """Model Tariff represents all tariff of the contract
    @param  periods     dict that represent a whole tariff, key is %Y%m%d%H
    """
    def __init__(self, tariff_type=TARIFF_TYPE_ENERGY, periods=None, name=None):
        if periods is None:
            periods = {}
        self.periods = periods
        self.tariff_type = tariff_type
        self.utils = CurveUtils()
        self.name = name

    def loadTariffPeriod(self, tariffPeriodList):
        """Load TariffPeriod to Tariff matrix {periods}
        Arguments:
            tariffPeriodList {[TariffPeriod]} -- List of TariffPeriod objects
        """
        for tariffPeriod in tariffPeriodList:
            start_time = tariffPeriod.start_time
            while start_time < tariffPeriod.end_time:
                if self.utils.getKeyDay(start_time) in self.periods:
                    raise Exception("Overlap tariff period")
                self.periods[self.utils.getKeyDay(start_time)] = tariffPeriod.kwh_price
                start_time += timedelta(hours=1)


class TariffPeriod:
    """Model TariffPeriod represents a tariff period on specific time and price
    @param  start_time      datetime(2020, 01, 01, 0)
    @param  end_time        datetime(2020, 01, 01, 0)
    @param  kwh_price       float(1.0)
    """
    def __init__(self, start_time, end_time, kwh_price):
        self.start_time = start_time
        self.end_time = end_time
        self.kwh_price = kwh_price

    def getPrice(self):
        return self.kwh_price

class CurveUtils:
    def getKeyDay(self, date, hour=0, format=None):
        if format is None:
            return int(datetime.strftime(date, "%Y%m%d%H"))
        if hour is not None:
            date_time = datetime.strptime(date, format) + timedelta(hours=hour)
        return int(datetime.strftime(date_time, "%Y%m%d%H"))

    def loadCurveFile(self, filename):
        import csv
        curves = {}
        with open(filename, newline='') as csvfile:
            next(csvfile) #Header
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                key = self.getKeyDay(row[1], int(row[2]), "%d/%m/%Y")
                value = float(row[3].replace(',','.'))
                curves[key] = value

        return curves

class TariffCalculator:
    def calculator(self, tariff_list, curves):
        """Calculator

        Arguments:
            tariff_list {[Tariff]} -- List of Tariff
            curves {dict()} -- Dict of curves

        Returns:
            String -- Name of Tariff
        """
        import sys
        lower_tariff_name = ""
        lower_tariff_amount = sys.float_info.max
        for tariff in tariff_list:
            amount = self.calculatorCurvePrice(tariff, curves)
            if amount < lower_tariff_amount:
                lower_tariff_amount = amount
                lower_tariff_name = tariff.name

        return lower_tariff_name

    def calculatorCurvePrice(self, tariff, curves):
        return 1



class TariffConstructor:
    """Imagine Tariff constructor
    """
    TARIFF = {
        "2.0_A": [[0,24,1,12, 0.139]],
        "2.0_DHA": [[0,12,1,3,0.082], [12,22,1,3,0.161], [22,24,1,3,0.082],
            [0,13,3,10,0.082], [13,23,3,10,0.161], [23,24,3,10,0.082],
            [0,12,10,12,0.082], [12,22,10,12,0.161],[22,24,10,12,0.082]]
    }
    HOUR_START = 0
    HOUR_END = 1
    MONTH_START = 2
    MONTH_END = 3
    PRICE = 4

    def getPrice(self, date_time, tariff):
        """[summary]

        Arguments:
            datetime {datetime} -- Datetime curve when hour is end hour of curve
            tariff {string} -- Name of tariff like 2.0_A, 2.0_DHA...

        Returns:
            float -- Amount price in tariff
        """
        price_list  = self.TARIFF[tariff]
        if len(price_list) == 1:
            return price_list[0][self.PRICE]

        for price in price_list:
            if price[self.HOUR_START] < date_time.hour and \
                price[self.HOUR_END] > date_time.hour and \
                price[self.MONTH_START] <= date_time.month and \
                price[self.MONTH_END] >= date_time.month:
                return price[self.PRICE]

        return 1