import logging
import time
import unittest
from datetime import datetime

from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.WeatherData import WeatherData


class TimeAndDateUtilTest(unittest.TestCase):
    """Unit tests for TimeAndDateUtil and related data containers."""

    @classmethod
    def setUpClass(cls):
        """Configure logging for the test run."""
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing TimeAndDateUtil and containers...")

    # ---------------- WeatherData container ----------------

    def testWeatherDataContainerDefaultValues(self):
        """WeatherData should initialize with sensible defaults."""
        wData = WeatherData()
        isoNow = TimeAndDateUtil.getCurrentIso8601LocalDate()

        self.assertEqual("", wData.source)
        self.assertEqual("", wData.url)
        self.assertEqual("", wData.description)

        self.assertEqual(0.0, wData.temperature)
        self.assertEqual(0.0, wData.humidity)
        self.assertEqual(0.0, wData.pressure)
        self.assertEqual(0.0, wData.windspeed)

        # timestamp should be near "now" (within 5 seconds)
        ts_a = datetime.fromisoformat(wData.timestamp).timestamp()
        ts_b = datetime.fromisoformat(isoNow).timestamp()
        self.assertAlmostEqual(ts_a, ts_b, delta=5.0)

        # location object should exist even if empty
        self.assertIsNotNone(wData.location)

    # ---------------- TimeAndDateUtil: current time ----------------

    def testGetCurrentIso8601LocalDate(self):
        """getCurrentIso8601LocalDate returns second-precision ISO8601."""
        curA = TimeAndDateUtil.getCurrentIso8601LocalDate()
        # Build expected value: local time, microseconds removed.
        curB = datetime.fromtimestamp(time.time()).replace(microsecond=0).isoformat()

        # May fail on very slow systems; values should match at second precision.
        self.assertEquals(curA, curB)

    # ---------------- TimeAndDateUtil: from millis ----------------

    def testGetIso8601DateFromMillis(self):
        """getIso8601DateFromMillis returns ISO8601 string for the millis input."""
        curSecs = time.time()
        curMillis = int(curSecs * 1000)

        isoA = TimeAndDateUtil.getIso8601DateFromMillis(curMillis)
        isoB = datetime.fromtimestamp(curSecs).replace(microsecond=0).isoformat()

        # May fail on very slow systems; values should match at second precision.
        self.assertEquals(isoA, isoB)


if __name__ == "__main__":
    unittest.main(verbosity=2)
