from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherData import WeatherData
from ipp.exercises.labmodule05.WeatherInfoContainer import (
    CloudLayerData,
    VisibilityData,
    WindData,
)


class WeatherDataParser:
    def __init__(self):
        pass

    def parseWeatherData(
        self,
        rawData: dict,
        stationID: str,
        stationName: str
    ) -> WeatherData:
        """
        Entry point for parsing.
        Takes the raw weather service response plus station metadata,
        and returns a WeatherData instance.
        """
        if rawData and stationID and stationName:
            return self._createWeatherDataFromRawData(
                rawData=rawData,
                stationID=stationID,
                stationName=stationName,
            )
        else:
            print("No raw data passed provided for parsing into WeatherData. Ignoring.")
            return None

    def _createWeatherDataFromRawData(
        self,
        rawData: dict,
        stationID: str,
        stationName: str
    ) -> WeatherData:
       
        pass
