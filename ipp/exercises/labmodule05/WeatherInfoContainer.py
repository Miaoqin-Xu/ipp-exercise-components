"""Containers for wind, visibility, and cloud layer info."""

class WindData:
    def __init__(self):
        self.speedKph = 0.0
        self.gustKph = 0.0
        self.directionDegrees = 0.0
    
class VisibilityData:
    def __init__(self):
        self.meters = 0.0

class CloudLayerData:
    def __init__(self):
        self.amount = 0.0
        self.baseMeters = 0.0