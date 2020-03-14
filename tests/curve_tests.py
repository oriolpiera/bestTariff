from besttariff.curve import *
from datetime import datetime, timedelta
import unittest

class CurveTest(unittest.TestCase):
    def test__dayOfWeek__Ok(self):
        c = Curve(datetime(2020, 1, 1, 0, 0), 0.0)

        d = c.dayOfWeek()

        self.assertEqual(d, 2)


class TariffPeriodTest(unittest.TestCase):
    def test__getPrice__Ok(self):
        tp = TariffPeriod(0,24,0, 0.131)

        price = tp.getPrice()

        self.assertEqual(price, 0.131)

if __name__ == '__main__':
    unittest.main()