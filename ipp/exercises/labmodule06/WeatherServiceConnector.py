import json
import requests

import ipp.common.ConfigConst as ConfigConst

from ipp.common.ConfigUtil import ConfigUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule06.WeatherDataParser import WeatherDataParser


class WeatherServiceConnector:
    WEATHER_SVC_SECTION_NAME = "Settings.Weather"

    def __init__(self, dataParser: WeatherDataParser = None):
        self.dataParser = dataParser
        self._initProperties()
    def _initProperties(self):
        self.configUtil = ConfigUtil()
        
        self.baseUrl = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "baseUrl")
        self.userAgent = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "userAgent")
        self.contentType = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "contentType")
        self.serviceName = \
            self.configUtil.getProperty( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "serviceName")
        self.pollRate = \
            self.configUtil.getInteger( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "pollCycleSecs")
        self.requestTimeout = \
            self.configUtil.getInteger( \
                WeatherServiceConnector.WEATHER_SVC_SECTION_NAME, "requestTimeoutSecs")
        
        self.latestRawData = None
        self.latestJsonData = None
        self.latestWeatherData = None

        self.clientSession = None
        self.isConnected = False

        print(f"Weather station name and URL -> {self.serviceName} {self.baseUrl}")

    def _createRequestUrl(
        self,
        stationID: str = None,
        locData: LocationData = None
    ):
        """
        Build and return the service-specific request URL based on a station ID
        and/or location data.

        Subclasses must implement.
        """
        pass

    def _getLatestWeatherData(
        self,
        requestUrl: str = None,
        stationID: str = None,
        locData: LocationData = None
    ) -> dict:
        """
        Perform the HTTP request (likely using requests or a session),
        parse the raw response into a dict, and return it.

        Subclasses must implement.
        """
        pass
    # ---------------------------
    # Connection management
    # ---------------------------

    def connectToService(self) -> bool:
        try:
            # Create a session for connection pooling
            self.clientSession = requests.Session()

            # Set default headers (required by most services)
            self.clientSession.headers.update({
                'User-Agent': self.userAgent,
                'Accept': self.contentType
            })

            return True

        except Exception as e:
            print(f"Connection to {self.serviceName} Weather Service failed: {e}")
            return False

    def disconnectFromService(self) -> bool:
        print(f"Disconnecting from weather service {self.serviceName}...")

        if self.clientSession:
            self.clientSession.close()
            self.clientSession = None
            self.isConnected = False

            print(f"Disconnected from {self.serviceName} Weather Service")
            return True

        return False
    # ---------------------------
    # Main action method
    # ---------------------------

    def requestCurrentWeatherData(
        self,
        stationID: str = None,
        locData: LocationData = None
    ) -> bool:

        requestUrl = self._createRequestUrl(
            stationID=stationID,
            locData=locData
        )

        responseData = self._getLatestWeatherData(
            requestUrl=requestUrl,
            stationID=stationID,
            locData=locData
        )

        if responseData:
            # store raw dict
            self.latestRawData = responseData

            # store pretty JSON text
            self.latestJsonData = json.dumps(self.latestRawData, indent=2)

            # run parser if one was provided
            if self.dataParser:
                self.latestWeatherData = self.dataParser.parseWeatherData(
                    rawData=responseData,
                    stationID=stationID,
                    stationName=locData.name if locData else None
                )

            print(
                f"Successfully retrieved current weather data from URL: {requestUrl}"
            )
            return True

        print(
            f"Failed to retrieve current weather data from URL: {requestUrl}"
        )
        return False
    # ---------------------------
    # Public-facing helper / getter methods
    # ---------------------------

    def getLatestWeatherData(self) -> WeatherData:
        return self.latestWeatherData

    def getLatestWeatherDataAsDict(self) -> dict:
        return self.latestRawData

    def getLatestWeatherDataAsJson(self) -> str:
        return self.latestJsonData

    def getPollRate(self) -> int:
        return self.pollRate

    def getRequestTimeout(self) -> int:
        return self.requestTimeout

    def getServiceName(self) -> str:
        return self.serviceName

    def getBaseUrl(self) -> str:
        return self.baseUrl

    def isClientConnected(self) -> bool:
        return self.isConnected