import logging
import unittest
from datetime import datetime

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData


class WeatherLocationDataTest(unittest.TestCase):
    """Unit tests for WeatherData and LocationData containers."""

    @classmethod
    def setUpClass(cls):
        """Configure logging for the test run."""
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing WeatherData and LocationData containers...")

    # ---------------- WeatherData: defaults ----------------

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

        # timestamps within 5 seconds (string → datetime → epoch seconds)
        ts_a = datetime.fromisoformat(wData.timestamp).timestamp()
        ts_b = datetime.fromisoformat(isoNow).timestamp()
        self.assertAlmostEqual(ts_a, ts_b, delta=5.0)

        # nested containers exist with defaults
        self.assertIsNotNone(wData.location)

    # ---------------- WeatherData: override all ----------------

    def testWeatherDataContainerOverrideAll(self):
        """Assign values to all primary fields and verify."""
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()
        locData = LocationData()
        wData = WeatherData()

        wData.source = "test"
        wData.url = "http://www.example.com"
        wData.description = "my weather site."
        wData.timestamp = isoTimeDate
        wData.temperature = 15.5
        wData.humidity = 54.9
        wData.pressure = 1018.0
        wData.windspeed = 14.0
        wData.conditions = "test"
        wData.icon = "http://www.example.com/icon.png"
        wData.location = locData

        self.assertEqual("test", wData.source)
        self.assertEqual("http://www.example.com", wData.url)
        self.assertEqual("my weather site.", wData.description)
        self.assertEqual(isoTimeDate, wData.timestamp)

        self.assertEqual(15.5, wData.temperature)
        self.assertEqual(54.9, wData.humidity)
        self.assertEqual(1018.0, wData.pressure)
        self.assertEqual(14.0, wData.windspeed)

        self.assertEqual("test", wData.conditions)
        self.assertEqual("http://www.example.com/icon.png", wData.icon)
        self.assertIs(wData.location, locData)

    # ---------------- LocationData: defaults ----------------

    def testLocationDataContainerDefaultValues(self):
        """LocationData should initialize with empty strings and zeros."""
        locData = LocationData()

        self.assertEqual("", locData.name)
        self.assertEqual("", locData.nameID)
        self.assertEqual("", locData.city)
        self.assertEqual("", locData.region)
        self.assertEqual("", locData.country)

        self.assertEqual(0.0, locData.latitude)
        self.assertEqual(0.0, locData.longitude)
        self.assertEqual(0.0, locData.elevation)

    # ---------------- LocationData: set values ----------------

    def testLocationDataContainerSetValues(self):
        """Assign values to LocationData and verify."""
        locData = LocationData()
        locData.name = "My Location"
        locData.city = "Boston"
        locData.region = "MA"
        locData.country = "US"
        locData.latitude = 42.0
        locData.longitude = -71.0
        locData.elevation = 10.0

        self.assertEqual("My Location", locData.name)
        self.assertEqual("Boston", locData.city)
        self.assertEqual("MA", locData.region)
        self.assertEqual("US", locData.country)

        self.assertEqual(42.0, locData.latitude)
        self.assertEqual(-71.0, locData.longitude)
        self.assertEqual(10.0, locData.elevation)


if __name__ == "__main__":
    unittest.main(verbosity=2)
