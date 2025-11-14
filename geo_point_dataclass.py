from dataclasses import dataclass

@dataclass
class GeoPoint:
    longitude: float
    latitude: float

    def __post_init__(self):
        if not -180 <= self.longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        if not 0 <= self.latitude <= 90:
            raise ValueError("Latitude must be between 0 and 90.")

