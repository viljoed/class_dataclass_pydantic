

from pydantic import BaseModel, field_validator

class GeoPoint(BaseModel):
    latitude: float
    longitude: float

    @field_validator("lon")
    def check_pairing(cls, lon, info):
        lat = info.data.get("lat")
        if (lat is None) != (lon is None):  # XOR
            raise ValueError("lat and lon must either both be set or both be None")
        return lon