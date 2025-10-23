from typing import List, Optional

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil
from ipp.exercises.labmodule05.LocationData import LocationData
from ipp.exercises.labmodule05.WeatherInfoContainer import CloudLayerData, VisibilityData, WindData


class WeatherData:
    """Container for weather data with sensible defaults."""
    def __init__(self):
        """Init fields; timestamp uses current ISO 8601."""
        self.source: str = ""
        self.url: str = ""
        self.description: str = ""
        self.timestamp: str = TimeAndDateUtil.getCurrentIso8601LocalDate()
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0
        self.windspeed: float = 0.0
        self.location: LocationData = LocationData()
        self.conditions: str = "N/A"
        self.icon: Optional[str] = None
        self.wind: WindData = WindData()
        self.visibility: VisibilityData = VisibilityData()
        self.cloudLayers: List[CloudLayerData] = []
