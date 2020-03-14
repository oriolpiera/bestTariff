from besttariff.curve import *
from datetime import datetime, timedelta
import unittest

class Test(unittest.TestCase):
    def test__dayOfWeek__Ok(self):
        c = Curve(datetime(2020, 1, 1, 0, 0), 0.0)

        d = c.dayOfWeek()

        self.assertEqual(d, 2)

if __name__ == '__main__':
    unittest.main()