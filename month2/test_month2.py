from contextlib import contextmanager
from datetime import date, timedelta
from locale import setlocale, LC_TIME
import unittest

from month2 import Month, MonthDelta


class MonthDeltaTests(unittest.TestCase):

    """Tests for MonthDelta."""

    def test_initializer(self):
        four_months = MonthDelta(4)
        self.assertEqual(four_months.months, 4)

    def test_equality(self):
        self.assertEqual(MonthDelta(12), MonthDelta(12))
        self.assertNotEqual(MonthDelta(11), MonthDelta(12))
        self.assertIs(MonthDelta(12) != MonthDelta(12), False)
        self.assertIs(MonthDelta(11) == MonthDelta(12), False)
        self.assertIs(MonthDelta(0) == timedelta(0), False)
        self.assertIs(MonthDelta(0) == 0, False)
        self.assertIs(MonthDelta(6) == 6, False)

    def test_adding_month_delta_to_unknown_value(self):
        with self.assertRaises(TypeError):
            MonthDelta(4) + 8
        with self.assertRaises(TypeError):
            8 + MonthDelta(4)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_adding_and_subtracting_with_monthdeltas(self):
        self.assertEqual(MonthDelta(4) + MonthDelta(2), MonthDelta(6))
        self.assertEqual(MonthDelta(4) - MonthDelta(2), MonthDelta(2))
        with self.assertRaises(TypeError):
            MonthDelta(4) - 8
        with self.assertRaises(TypeError):
            8 - MonthDelta(4)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_scaling_and_division(self):
        self.assertEqual(MonthDelta(4) * 2, MonthDelta(8))
        self.assertEqual(2 * MonthDelta(4), MonthDelta(8))
        self.assertEqual(MonthDelta(4) / 2, MonthDelta(2))
        self.assertEqual(MonthDelta(4) / MonthDelta(2), 2)
        self.assertEqual(MonthDelta(18) // 12, MonthDelta(1))
        self.assertEqual(MonthDelta(18) // MonthDelta(12), 1)
        self.assertEqual(MonthDelta(18) % MonthDelta(12), 6)
        self.assertEqual(MonthDelta(18) % 12, MonthDelta(6))
        self.assertEqual(-MonthDelta(18), MonthDelta(-18))
        with self.assertRaises(TypeError):
            MonthDelta(4) * "a"
        with self.assertRaises(TypeError):
            MonthDelta(4) * 2.0
        with self.assertRaises(TypeError):
            MonthDelta(4) / 2.0
        with self.assertRaises(TypeError):
            MonthDelta(4) * MonthDelta(2)
        with self.assertRaises(TypeError):
            MonthDelta(4) % 0.5


class MonthTests(unittest.TestCase):

    """Tests for Month."""

    def test_initializer(self):
        python2_eol = Month(2020, 1)
        self.assertEqual(python2_eol.year, 2020)
        self.assertEqual(python2_eol.month, 1)

    def test_equality(self):
        python2_eol = Month(2020, 1)
        self.assertEqual(python2_eol, Month(2020, 1))
        self.assertNotEqual(python2_eol, Month(2020, 2))
        self.assertNotEqual(python2_eol, Month(2019, 1))
        self.assertIs(python2_eol != Month(2020, 1), False)
        self.assertIs(python2_eol == Month(2020, 2), False)
        self.assertNotEqual(python2_eol, date(2020, 1, 1))
        self.assertNotEqual(python2_eol, (2020, 1))
        self.assertIs(Month(2020, 1) == date(2020, 1, 1), False)

    def test_month_arithmetic_with_month_deltas(self):
        python2_eol = Month(2020, 1)
        python2_release = Month(2000, 10)
        python2_lifetime = MonthDelta(231)
        self.assertEqual(python2_eol + MonthDelta(4), Month(2020, 5))
        self.assertEqual(MonthDelta(13) + python2_eol, Month(2021, 2))
        self.assertEqual(python2_eol - MonthDelta(4), Month(2019, 9))
        self.assertEqual(python2_eol - MonthDelta(13), Month(2018, 12))
        self.assertEqual(python2_release + python2_lifetime, python2_eol)

    def test_month_subtracting_months(self):
        python2_eol = Month(2020, 1)
        python2_release = Month(2000, 10)
        python2_lifetime = python2_eol - python2_release
        self.assertEqual(python2_lifetime, MonthDelta(20*12 - 9))

    def test_arithmetic_with_other_types(self):
        python2_eol = Month(2020, 1)
        python2_release = Month(2000, 10)
        python2_lifetime = python2_eol - python2_release
        with self.assertRaises(TypeError):
            python2_eol + python2_release
        with self.assertRaises(TypeError):
            python2_eol * python2_release
        with self.assertRaises(TypeError):
            python2_eol * python2_lifetime
        with self.assertRaises(TypeError):
            python2_lifetime - python2_eol
        with self.assertRaises(TypeError):
            python2_eol - date(1999, 12, 1)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_formatting(self):
        python2_eol = Month(2020, 1)
        leap_month = Month(2000, 2)
        self.assertEqual("{:%Y-%m}".format(python2_eol), "2020-01")
        with set_locale('C'):
            self.assertEqual("{0:%b %Y}".format(leap_month), "Feb 2000")
            self.assertEqual("{:%b %Y}".format(python2_eol), "Jan 2020")


@contextmanager
def set_locale(name):
    saved = setlocale(LC_TIME)
    try:
        yield setlocale(LC_TIME, name)
    finally:
        setlocale(LC_TIME, saved)


if __name__ == "__main__":
    unittest.main(verbosity=2)