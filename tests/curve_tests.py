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

class OldTariffTests(unittest.TestCase):
    def test__loadTariffPeriod__oneOk(self):
        tp = TariffPeriod(0,23,0, 0.131)
        t = OldTariff()

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
        t = OldTariff()

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
        t = OldTariff()
        with self.assertRaises(Exception) as cm:
            t.loadTariffPeriod([tp1,tp2])

        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Overlap tariff period")

    def test__loadTariffPeriod__isCompleted(self):
        tp1 = TariffPeriod(0,23,0, 0.131)
        t = OldTariff()
        t.loadTariffPeriod([TariffPeriod(0,23,0, 0.131),
        TariffPeriod(0,23,1, 0.131),
        TariffPeriod(0,23,2, 0.131),
        TariffPeriod(0,23,3, 0.131),
        TariffPeriod(0,23,4, 0.131),
        TariffPeriod(0,23,5, 0.131),
        TariffPeriod(0,23,6, 0.131)])

        self.assertTrue(t.isCompleted())

    def test__loadTariffPeriod__isNotCompleted(self):
        tp1 = TariffPeriod(0,12,0, 0.131)
        tp2 = TariffPeriod(13,23,0, 0.132)
        t = OldTariff()
        t.loadTariffPeriod([tp1,tp2])

        self.assertFalse(t.isCompleted())

class TariffTests(unittest.TestCase):
    def test__getKeyDay__datetime(self):
        t = Tariff()

        key = t.getKeyDay(datetime(2020, 1, 1))

        self.assertEqual(key, 1577836800)

    def test__getKeyDay__string(self):
        t = Tariff()

        key = t.getKeyDay("01/01/2020", "%d/%m/%Y")

        self.assertEqual(key, 1577836800)

if __name__ == '__main__':
    unittest.main()