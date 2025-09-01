##
# MIT License
# 
# Copyright (c) 2020 - 2025 Andrew D. King
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import logging
import os
import unittest

import ipp.common.ConfigConst as ConfigConst

from ipp.common.ConfigUtil import ConfigUtil

class ConfigUtilCustomTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	ConfigUtil. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	DEFAULT_USER = "Foo"
	DEFAULT_AUTH = "Bar"
	
	# optionally test the following files
	#  - EmptyTestConfig.props
	#  - InvalidTestConfig.props
	#  - None (which will default to ./config/IppConfig.props)
	configFile = os.path.dirname(__file__) + "/ValidTestConfig.props"
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing ConfigUtil class (custom file load)...")

		self.configUtil = ConfigUtil(configFile = self.configFile)
		
	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def testGetBooleanProperty(self):
		enableLogging = self.configUtil.hasProperty(ConfigConst.IPP_TEST_APP, ConfigConst.ENABLE_LOGGING_KEY)
		self.assertTrue(enableLogging)
	
	def testGetIntegerProperty(self):
		port = self.configUtil.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY)
		self.assertEqual(port, ConfigConst.DEFAULT_MQTT_PORT)
	
	def testGetFloatProperty(self):
		hSimFloor = self.configUtil.getFloat(ConfigConst.IPP_TEST_APP, ConfigConst.HUMIDITY_SIM_FLOOR_KEY)
		self.assertGreater(hSimFloor, 0.0)
	
	def testGetProperty(self):
		hostName = self.configUtil.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY)
		self.assertTrue(hostName)
	
	def testHasProperty(self):
		self.assertTrue(self.configUtil.hasProperty(ConfigConst.IPP_TEST_APP, ConfigConst.ENABLE_EMULATOR_KEY))

	def testHasSection(self):
		self.assertTrue(self.configUtil.hasSection(ConfigConst.IPP_TEST_APP))
	
	def testIsConfigDataLoaded(self):
		self.assertTrue(self.configUtil.isConfigDataLoaded())
	
if __name__ == "__main__":
	unittest.main()
