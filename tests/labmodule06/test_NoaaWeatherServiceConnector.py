import logging
import time
import unittest

from ipp.exercises.labmodule05.LocationData import LocationData

from ipp.exercises.labmodule06.NoaaWeatherServiceConnector import NoaaWeatherServiceConnector

class NoaaWeatherServiceConnectorTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing NoaaWeatherServiceConnector class...")
		
	def setUp(self):
		self.weatherSvc = NoaaWeatherServiceConnector()
		self.assertTrue(self.weatherSvc.connectToService())#Temperary fix to avoid connection issues in tests

	def tearDown(self):
		pass
	
	def testWeatherServiceConnection(self):
		self.assertTrue(self.weatherSvc.connectToService())
		time.sleep(5)

		self.assertTrue(self.weatherSvc.disconnectFromService())
		
	def testWeatherServiceRequestByStation(self):
		locData = self._createSampleLocationData()
		
		self.assertTrue(self.weatherSvc.connectToService())
		time.sleep(5)

		self.assertTrue(self.weatherSvc.requestCurrentWeatherData(stationID = "KBOS", locData = locData))

		jsonData = self.weatherSvc.getLatestWeatherDataAsJson()
		
		print(jsonData)

		self.assertIsNotNone(jsonData)
		time.sleep(5)

		self.assertTrue(self.weatherSvc.disconnectFromService())
		
	def testWeatherServiceProperties(self):
		self.assertEqual(self.weatherSvc.getServiceName(), "NOAA Weather Service")

		# TODO: Add other properties
	
	def _createSampleLocationData(self) -> LocationData:
		locData = LocationData()
		locData.name = "KBOS"
		locData.city = "Boston"
		locData.region = "MA"
		locData.country = "USA"
		locData.latitude = 42.35843
		locData.longitude = -71.05977

		return locData