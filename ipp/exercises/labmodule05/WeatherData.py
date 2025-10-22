"""Weather data container.

Holds source metadata, observation values, and nested containers for wind,
visibility, and cloud layers. Timestamps are stored as local ISO 8601 strings.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .TimeAndDateUtil import TimeAndDateUtil
from .LocationData import LocationData
from .WeatherInfoContainer import CloudLayerData, VisibilityData, WindData


@dataclass
class WeatherData:
    """Lightweight container for a weather observation.

    Public attributes:
    source      -- name of the data source (str)
    url         -- URL for the originating resource (str)
    description -- human-readable description (str)
    timestamp   -- ISO 8601 local date/time string (str)
    temperature -- air temperature in °C (float)
    humidity    -- relative humidity in percent (float)
    pressure    -- pressure in hPa (float)
    windspeed   -- wind speed in km/h (float)
    location    -- LocationData object (LocationData)
    conditions  -- textual summary, e.g., 'Clear' (str)
    icon        -- optional icon code/string (str or None)
    wind        -- wind details (WindData)
    visibility  -- horizontal visibility (VisibilityData)
    cloudLayers -- list of cloud layers (List[CloudLayerData])
    """

    source: str = ""
    url: str = ""
    description: str = ""
    timestamp: str = field(
        default_factory=lambda: TimeAndDateUtil.getCurrentIso8601LocalDate()
    )
    temperature: float = 0.0
    humidity: float = 0.0
    pressure: float = 0.0
    windspeed: float = 0.0
    location: LocationData = field(default_factory=LocationData)
    conditions: str = "N/A"
    icon: Optional[str] = None
    wind: WindData = field(default_factory=WindData)
    visibility: VisibilityData = field(default_factory=VisibilityData)
    cloudLayers: List[CloudLayerData] = field(default_factory=list)
