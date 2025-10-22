import logging
import unittest

from ipp.exercises.labmodule05.CalculationsUtil import CalculationsUtil


class CalculationsUtilTest(unittest.TestCase):
    """Unit tests for CalculationsUtil."""

    @classmethod
    def setUpClass(cls):
        """Configure logging for the test run."""
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing CalculationsUtil class...")

    def setUp(self):
        """Run before each test."""
        pass

    def tearDown(self):
        """Run after each test."""
        pass

    # --- divideTwoNumbers -------------------------------------------------

    def testDivideTwoIntegers(self):
        """Divide integers, including zero denominator case."""
        cases = [
            ((1, 0), 0.0),
            ((10, 2), 5.0),
            ((10, 5), 2.0),
            ((10, 10), 1.0),
            ((-9, 3), -3.0),
        ]
        for (n, d), expected in cases:
            with self.subTest(n=n, d=d):
                self.assertEqual(expected, CalculationsUtil.divideTwoNumbers(n, d))

    def testDivideTwoFloats(self):
        """Divide floats, including zero denominator case."""
        cases = [
            ((1.5, 0.0), 0.0),
            ((11.0, 2.0), 5.5),
            ((5.0, 2.0), 2.5),
            ((1.5, 1.0), 1.5),
            ((-3.0, 0.5), -6.0),
        ]
        for (n, d), expected in cases:
            with self.subTest(n=n, d=d):
                self.assertAlmostEqual(
                    CalculationsUtil.divideTwoNumbers(n, d), expected, places=9
                )

    # --- temperature conversions -----------------------------------------

    def testFarenheitToCelsiusConversion(self):
        """Check F→C against known pairs."""
        pairs = [
            (212.0, 100.0),
            (32.0, 0.0),
            (98.6, 37.0),
            (14.0, -10.0),
            (-40.0, -40.0),
        ]
        for f, c_expected in pairs:
            with self.subTest(F=f):
                self.assertAlmostEqual(
                    CalculationsUtil.convertTempFtoC(f), c_expected, places=6
                )

    def testCelsiusToFarenheitConversion(self):
        """Check C→F against known pairs."""
        pairs = [
            (100.0, 212.0),
            (0.0, 32.0),
            (37.0, 98.6),
            (-10.0, 14.0),
            (-40.0, -40.0),
        ]
        for c, f_expected in pairs:
            with self.subTest(C=c):
                self.assertAlmostEqual(
                    CalculationsUtil.convertTempCtoF(c), f_expected, places=6
                )

    def testRoundTripTemperatureConversion(self):
        """Converting C→F→C returns the original value within tolerance."""
        for c in [-40.0, -10.0, 0.0, 20.5, 37.0, 100.0]:
            with self.subTest(C=c):
                f = CalculationsUtil.convertTempCtoF(c)
                back = CalculationsUtil.convertTempFtoC(f)
                self.assertAlmostEqual(back, c, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
