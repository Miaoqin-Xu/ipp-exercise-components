import logging
import unittest
from datetime import datetime

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData


class WeatherAndLocationDataTest(unittest.TestCase):
    """Unit tests for WeatherData and LocationData containers."""

    @classmethod
    def setUpClass(cls):
        """Configure logging once for the test class."""
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing WeatherData and LocationData containers...")

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

    def testWeatherDataContainerCustomValues(self):
        """WeatherData accepts custom field values."""
        isoTimeDate = TimeAndDateUtil.getCurrentIso8601LocalDate()
        locData = LocationData()
        wData = WeatherData()

        wData.source = "test"
        wData.url = "https://www.example.com"
        wData.description = "My weather site."
        wData.timestamp = isoTimeDate
        wData.temperature = 15.0
        wData.humidity = 45.0
        wData.pressure = 1005.0
        wData.windspeed = 5.0
        wData.location = locData

        self.assertEqual(wData.source, "test")
        self.assertEqual(wData.url, "https://www.example.com")
        self.assertEqual(wData.description, "My weather site.")
        self.assertEqual(wData.timestamp, isoTimeDate)

        self.assertEqual(wData.temperature, 15.0)
        self.assertEqual(wData.humidity, 45.0)
        self.assertEqual(wData.pressure, 1005.0)
        self.assertEqual(wData.windspeed, 5.0)

        self.assertEqual(wData.location, locData)

        # TODO: add other tests if you'd like

    def testLocationDataContainerDefaultValues(self):
        """LocationData default values (empty strings and zeros)."""
        locData = LocationData()

        self.assertEqual(locData.name, "")
        self.assertEqual(locData.city, "")
        self.assertEqual(locData.region, "")
        self.assertEqual(locData.country, "")

        self.assertEqual(locData.latitude, 0.0)
        self.assertEqual(locData.longitude, 0.0)
        self.assertEqual(locData.elevation, 0.0)

        # TODO: add other tests if you'd like

    def testLocationDataContainerCustomValues(self):
        """LocationData assigns and reads custom strings."""
        locData = LocationData()

        locData.name = "My Location"
        locData.city = "Boston"
        locData.region = "MA"
        locData.country = "USA"

        self.assertEqual(locData.name, "My Location")
        self.assertEqual(locData.city, "Boston")
        self.assertEqual(locData.region, "MA")
        self.assertEqual(locData.country, "USA")

        # TODO: add other tests if you'd like
