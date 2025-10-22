"""Location data container.

Holds basic identity and geospatial attributes for a location.
"""

from dataclasses import dataclass

# The lab asks to import TimeAndDateUtil. It is not used directly here,
# but keeping the import available for callers and future extensions.
from .TimeAndDateUtil import TimeAndDateUtil  # noqa: F401


@dataclass
class LocationData:
    """Lightweight container for a location.

    Public attributes:
    name       -- human-readable name of the location (str)
    nameID     -- identifier for the location, e.g., station ID (str)
    city       -- city name (str)
    region     -- state/province/region name (str)
    country    -- country name (str)
    latitude   -- latitude in decimal degrees (float)
    longitude  -- longitude in decimal degrees (float)
    elevation  -- elevation in meters (float)
    """

    name: str = ""
    nameID: str = ""
    city: str = ""
    region: str = ""
    country: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    elevation: float = 0.0
