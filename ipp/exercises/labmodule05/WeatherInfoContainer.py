"""Weather information containers.

Defines lightweight containers for wind, visibility, and cloud-layer data.
"""

from typing import Optional


class WindData:
    """Container for wind information.

    Keyword arguments:
    speedKph -- sustained wind speed in kilometers per hour (float or None)
    gustKph -- gust speed in kilometers per hour (float or None)
    directionDegrees -- wind direction in degrees, 0..360 (float or None)

    Public attributes:
    speedKph, gustKph, directionDegrees
    """

    def __init__(
        self,
        speedKph: Optional[float] = None,
        gustKph: Optional[float] = None,
        directionDegrees: Optional[float] = None,
    ):
        self.speedKph = speedKph
        self.gustKph = gustKph
        self.directionDegrees = directionDegrees


class VisibilityData:
    """Container for horizontal visibility.

    Keyword arguments:
    meters -- visibility distance in meters (float or None)

    Public attributes:
    meters
    """

    def __init__(self, meters: Optional[float] = None):
        self.meters = meters


class CloudLayerData:
    """Container describing a single cloud layer.

    Keyword arguments:
    amount -- qualitative coverage, e.g., "FEW", "SCT", "BKN", "OVC"
    baseMeters -- cloud base height above ground in meters (float or None)

    Public attributes:
    amount, baseMeters
    """

    def __init__(self, amount: str, baseMeters: Optional[float] = None):
        self.amount = amount
        self.baseMeters = baseMeters
