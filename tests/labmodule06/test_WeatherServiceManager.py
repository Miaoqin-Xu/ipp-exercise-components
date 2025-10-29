import datetime
import logging
import time
import unittest

from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.WeatherData import WeatherData

from ipp.exercises.labmodule06.WeatherServiceManager import WeatherServiceManager

class WeatherServiceManagerTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing WeatherServiceManager class...")
		
	def setUp(self):
		self.weatherSvcMgr = WeatherServiceManager()

	def tearDown(self):
		pass
	
	def testWeatherServiceManagerExecution(self):
		self.weatherSvcMgr.startManager()

		# let it run for ~2 min's
		time.sleep(120)

		self.weatherSvcMgr.stopManager()