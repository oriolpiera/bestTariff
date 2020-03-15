from besttariff.curve import *
from datetime import datetime, timedelta
import unittest
import numpy as np

class CurveTests(unittest.TestCase):
    def test__dayOfWeek__Ok(self):
        c = Curve(datetime(2020, 1, 1, 0, 0), 0.0)

        d = c.dayOfWeek()

        self.assertEqual(d, 2)

class TariffTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test__loadTariffPeriod__oneOk(self):
        t = Tariff()
        tp = TariffPeriod(datetime(2020, 1, 1, 0),
        datetime(2020, 1, 1, 1), 0.131)

        t.loadTariffPeriod([tp])

        self.assertDictEqual(t.periods,{2020010100: 0.131})

    def test__loadTariffPeriod__nOk(self):
        t = Tariff()

        t.loadTariffPeriod([
            TariffPeriod(datetime(2020, 1, 1, 0),datetime(2020, 1, 1, 11), 0.131),
            TariffPeriod(datetime(2020, 1, 1, 11),datetime(2020, 1, 1, 22), 0.078),
            TariffPeriod(datetime(2020, 1, 1, 22),datetime(2020, 1, 2, 0), 0.131),
        ])

        self.assertDictEqual(t.periods, {2020010100: 0.131, 2020010101: 0.131,
            2020010102: 0.131, 2020010103: 0.131, 2020010104: 0.131,
            2020010105: 0.131, 2020010106: 0.131, 2020010107: 0.131,
            2020010108: 0.131, 2020010109: 0.131, 2020010110: 0.131,
            2020010111: 0.078, 2020010112: 0.078, 2020010113: 0.078,
            2020010114: 0.078, 2020010115: 0.078, 2020010116: 0.078,
            2020010117: 0.078, 2020010118: 0.078, 2020010119: 0.078,
            2020010120: 0.078, 2020010121: 0.078, 2020010122: 0.131,
            2020010123: 0.131})

    def test__loadTariffPeriod__overlapException(self):
        t = Tariff()

        with self.assertRaises(Exception) as cm:
            t.loadTariffPeriod([
                TariffPeriod(datetime(2020, 1, 1, 0),datetime(2020, 1, 1, 11), 0.131),
                TariffPeriod(datetime(2020, 1, 1, 10),datetime(2020, 1, 1, 22), 0.078),
                TariffPeriod(datetime(2020, 1, 1, 22),datetime(2020, 1, 2, 0), 0.131),
            ])

        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Overlap tariff period")

class TariffPeriodTests(unittest.TestCase):
    def test__getPrice__Ok(self):
        tp = TariffPeriod(datetime(2020, 1, 1),
            datetime(2020, 1, 1), 0.131)

        price = tp.getPrice()

        self.assertEqual(price, 0.131)

class CurveUtilsTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test__getKeyDay__datetime(self):
        cu = CurveUtils()

        key = cu.getKeyDay(datetime(2020, 1, 1))

        self.assertEqual(key, 2020010100)

    def test__getKeyDay__string(self):
        cu = CurveUtils()

        key = cu.getKeyDay("01/01/2020", 0, "%d/%m/%Y")

        self.assertEqual(key, 2020010100)

    def test__loadCurveFile__Ok(self):
        cu = CurveUtils()

        curve_dict = cu.loadCurveFile("./tests/sample_curve_file.csv")

        self.assertEqual(curve_dict, {2019010101: 1.308,
            2019010102: 0.455, 2019010103: 0.42, 2019010104: 0.383,
            2019010105: 0.356, 2019010106: 0.341, 2019010107: 0.352,
            2019010108: 0.357, 2019010109: 0.353})

class TariffCalculatorTests(unittest.TestCase):
    def test__calculator__ok(self):
        tc = TariffCalculator()
        tariff = Tariff(TARIFF_TYPE_ENERGY, {2020010100: 0.131, 2020010101: 0.131,
            2020010102: 0.131, 2020010103: 0.131, 2020010104: 0.131,
            2020010105: 0.131, 2020010106: 0.131, 2020010107: 0.131,
            2020010108: 0.131, 2020010109: 0.131, 2020010110: 0.131,
            2020010111: 0.078, 2020010112: 0.078, 2020010113: 0.078,
            2020010114: 0.078, 2020010115: 0.078, 2020010116: 0.078,
            2020010117: 0.078, 2020010118: 0.078, 2020010119: 0.078,
            2020010120: 0.078, 2020010121: 0.078, 2020010122: 0.131,
            2020010123: 0.131}, "2.0_DHA")
        cu = CurveUtils()
        curves = cu.loadCurveFile("./tests/sample_curve_file_20200101.csv")

        value = tc.calculator([tariff], curves)

        self.assertEqual(value, "2.0_DHA")

if __name__ == '__main__':
    unittest.main()