"""Containers for wind, visibility, and cloud layer info."""

from typing import Optional


class WindData:
    """Wind measurements in kph and direction degrees."""
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
    """Visibility distance in meters."""
    def __init__(self, meters: Optional[float] = None):
        self.meters = meters


class CloudLayerData:
    """Cloud layer amount and base height in meters."""
    def __init__(self, amount: str, baseMeters: Optional[float] = None):
        self.amount = amount
        self.baseMeters = baseMeters
