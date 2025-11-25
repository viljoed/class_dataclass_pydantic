from pydantic import BaseModel, Field

class GeoPoint(BaseModel):
    longitude: float = Field(ge=-180, le=180)
    latitude: float = Field(ge=0, le=90)






