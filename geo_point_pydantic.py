from pydantic import BaseModel, field_validator, ValidationError

class GeoPoint(BaseModel):
    longitude: float
    latitude: float

    @field_validator("longitude")
    def validate_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return v

    @field_validator("latitude")
    def validate_latitude(cls, v):
        if not 0 <= v <= 90:
            raise ValueError("Latitude must be between 0 and 90.")
        return v



