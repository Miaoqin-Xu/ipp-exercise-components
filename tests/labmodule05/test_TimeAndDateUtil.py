import logging
import unittest
import time
from datetime import datetime

from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.WeatherData import WeatherData


class TimeAndDateUtilTest(unittest.TestCase):
    """Unit tests for TimeAndDateUtil and WeatherData."""

    def testWeatherDataContainerDefaultValues(self):
        """WeatherData defaults and timestamp close to now (±5s)."""
        wData = WeatherData()
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()

        self.assertEqual(wData.source, "")
        self.assertEqual(wData.url, "")
        self.assertEqual(wData.description, "")

        self.assertEqual(wData.temperature, 0.0)
        self.assertEqual(wData.humidity, 0.0)
        self.assertEqual(wData.pressure, 0.0)
        self.assertEqual(wData.windspeed, 0.0)

        timestampA = datetime.fromisoformat(wData.timestamp).timestamp()
        timestampB = datetime.fromisoformat(isoTimeDate).timestamp()
        # assert they're within 5 seconds
        self.assertAlmostEqual(timestampA, timestampB, delta=5.0)

        self.assertIsNotNone(wData.location)

        # TODO: add other tests if you'd like

    def testGetCurrentIso8601LocalDate(self):
        """Current ISO 8601 string equals system time (seconds precision)."""
        curIso8601DateA = TimeAndDateUtil.getCurrentIso8601LocalDate()
        curIso8601DateB = datetime.fromtimestamp(time.time()).replace(microsecond=0).isoformat()

        # this may fail on REALLY slow systems
        self.assertEqual(curIso8601DateA, curIso8601DateB)

        # TODO: add other tests if you'd like

    def testGetIso8601DateFromMillis(self):
        """Format ISO 8601 string from epoch milliseconds."""
        curDateInSecs = time.time()

        curIso8601DateA = TimeAndDateUtil.getIso8601DateFromMillis(curDateInSecs * 1000)
        curIso8601DateB = datetime.fromtimestamp(curDateInSecs).replace(microsecond=0).isoformat()

        # this may fail on REALLY slow systems
        self.assertEqual(curIso8601DateA, curIso8601DateB)

        # TODO: add other tests if you'd like

# if __name__ == "__main__":
#     unittest.main()