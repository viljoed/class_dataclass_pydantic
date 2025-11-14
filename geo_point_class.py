class GeoPoint:
    def __init__(self, longitude: float, latitude: float):
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        if not 0 <= latitude <= 90:
            raise ValueError("Latitude must be between 0 and 90.")
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return f"GeoPoint(longitude={self.longitude}, latitude={self.latitude})"