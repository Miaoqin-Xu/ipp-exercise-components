from ipp.exercises.labmodule05.WeatherData import WeatherData


class WeatherDataListener:
    def __init__(self):
        pass

    def handleIncomingWeatherData(self, data: WeatherData = None):
        """
        This is called by the weather service whenever new weather data arrives.
        It forwards the data to the internal processing hook.
        """
        if data:
            self._processWeatherData(wData=data)

    def _processWeatherData(self, wData: WeatherData = None):
        pass
