import logging
import unittest

from ipp.exercises.labmodule05.CalculationsUtil import CalculationsUtil


class CalculationsUtilTest(unittest.TestCase):
    """Unit tests for CalculationsUtil."""

    @classmethod
    def setUpClass(cls):
        """Configure logging for this test class."""
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing CalculationsUtil class...")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDivideTwoIntegers(self):
        """Divide integers, including divide-by-zero returning 0.0."""
        self.assertEqual(0.0, CalculationsUtil.divideTwoNumbers(1, 0))
        self.assertEqual(5.0, CalculationsUtil.divideTwoNumbers(10, 2))
        self.assertEqual(2.0, CalculationsUtil.divideTwoNumbers(10, 5))
        self.assertEqual(1.0, CalculationsUtil.divideTwoNumbers(10, 10))

        # TODO: Add other tests if you'd like

    def testDivideTwoFloats(self):
        """Divide floats, including divide-by-zero returning 0.0."""
        self.assertEqual(0.0, CalculationsUtil.divideTwoNumbers(1.5, 0))
        self.assertEqual(5.5, CalculationsUtil.divideTwoNumbers(11, 2))
        self.assertEqual(2.5, CalculationsUtil.divideTwoNumbers(5, 2))
        self.assertEqual(1.5, CalculationsUtil.divideTwoNumbers(1.5, 1.0))

        # TODO: Add other tests if you'd like

    def testFarhenheitToCelsiusConversion(self):
        """Convert Fahrenheit to Celsius at key landmarks and a common value."""
        # 32F -> 0C
        self.assertAlmostEqual(0.0, CalculationsUtil.fahrenheitToCelsius(32.0), places=7)
        # 212F -> 100C
        self.assertAlmostEqual(100.0, CalculationsUtil.fahrenheitToCelsius(212.0), places=7)
        # -40F -> -40C (invariant point)
        self.assertAlmostEqual(-40.0, CalculationsUtil.fahrenheitToCelsius(-40.0), places=7)
        # 98.6F -> ~37C (body temperature)
        self.assertAlmostEqual(37.0, CalculationsUtil.fahrenheitToCelsius(98.6), places=7)

        pass

    def testCelsiusToFarenheitConversion(self):
        """Convert Celsius to Fahrenheit at key landmarks and a common value."""
        # 0C -> 32F
        self.assertAlmostEqual(32.0, CalculationsUtil.celsiusToFahrenheit(0.0), places=7)
        # 100C -> 212F
        self.assertAlmostEqual(212.0, CalculationsUtil.celsiusToFahrenheit(100.0), places=7)
        # -40C -> -40F (invariant point)
        self.assertAlmostEqual(-40.0, CalculationsUtil.celsiusToFahrenheit(-40.0), places=7)
        # 37C -> ~98.6F (body temperature)
        self.assertAlmostEqual(98.6, CalculationsUtil.celsiusToFahrenheit(37.0), places=7)

        pass
