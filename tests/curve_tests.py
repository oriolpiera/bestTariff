from besttariff.curve import *
from datetime import datetime, timedelta
import unittest
import numpy as np

class CurveTests(unittest.TestCase):
    def test__dayOfWeek__Ok(self):
        c = Curve(datetime(2020, 1, 1, 0, 0), 0.0)

        d = c.dayOfWeek()

        self.assertEqual(d, 2)


class TariffPeriodTests(unittest.TestCase):
    def test__getPrice__Ok(self):
        tp = TariffPeriod(0,23,0, 0.131)

        price = tp.getPrice()

        self.assertEqual(price, 0.131)

class TariffTests(unittest.TestCase):
    def test__loadTariffPeriod__oneOk(self):
        tp = TariffPeriod(0,23,0, 0.131)
        t = Tariff()

        t.loadTariffPeriod([tp])

        np.testing.assert_array_equal(t.getMatrix(),
            [[0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

    def test__loadTariffPeriod__twoOk(self):
        tp1 = TariffPeriod(0,23,0, 0.131)
        tp2 = TariffPeriod(0,23,1, 0.132)
        t = Tariff()

        t.loadTariffPeriod([tp1,tp2])

        np.testing.assert_array_equal(t.getMatrix(),
            [[0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131,
            0.131,0.131,0.131,0.131,0.131,0.131],
            [0.132,0.132,0.132,0.132,0.132,0.132,
            0.132,0.132,0.132,0.132,0.132,0.132,
            0.132,0.132,0.132,0.132,0.132,0.132,
            0.132,0.132,0.132,0.132,0.132,0.132],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

    def test__loadTariffPeriod__overlapException(self):
        tp1 = TariffPeriod(0,12,0, 0.131)
        tp2 = TariffPeriod(12,23,0, 0.132)
        t = Tariff()
        with self.assertRaises(Exception) as cm:
            t.loadTariffPeriod([tp1,tp2])

        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Overlap tariff period")

if __name__ == '__main__':
    unittest.main()