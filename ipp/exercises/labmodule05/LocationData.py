"""Simple data container for location metadata."""

from ipp.exercises.labmodule05.TimeAndDateUtil import TimeAndDateUtil  # imported per spec

class LocationData():
    """Container for basic location fields."""

    def __init__(self):
        """Initialize fields to empty strings and zeros."""
        self.name: str = ""
        self.nameID: str = ""
        self.city: str = ""
        self.region: str = ""
        self.country: str = ""
        self.latitude: float = 0.0
        self.longitude: float = 0.0
        self.elevation: float = 0.0
