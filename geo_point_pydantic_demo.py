from pydantic import BaseModel
from geo_point_pydantic import GeoPoint
import common
from datetime import date

common.run(GeoPoint)

# Output:
# longitude=-75.7552 latitude=45.3484
# 2 validation errors for GeoPoint
# longitude
#   Value error, Longitude must be between -180 and 180. [type=value_error, input_value=500, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/value_error
# latitude
#   Value error, Latitude must be between 0 and 90. [type=value_error, input_value=200, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/value_error

print("Pydantic specific features")
print("==========================")

# Coercion (str -> float)
# Since 
# class GeoPoint(BaseModel):
    # longitude: float
    # latitude: float
longitude, latitude = "-75.7552", 45.3484
pnt = GeoPoint(longitude=longitude, latitude=latitude)
print(pnt)

print("\n.model_dump()")
print("- Returns a plain Python dict")
print("- Suitable for internal use, logic, or non-JSON-specific processing")
print("- Uses raw Python values (e.g., datetime, Decimal, Enum, etc.)")
print("==========================")
print(pnt.model_dump())

print("\n.model_dump_json()")
print("Returns JSON string of the model data")
print("==========================")
print(pnt.model_dump_json())

print("\n.model_dump_json(indent=2)")
print("Returns JSON string of the model data with indentation")
print("==========================")
print(pnt.model_dump_json(indent=2))

print("model_dump(mode='json')")
print("Returns a dict with values prepared for JSON serialization")
print("Converts non-JSON types (e.g., datetime → ISO string, Enum → value)")
print("==========================")
print(pnt.model_dump(mode='json'))

print("\nModel from json, i.e. GeoPoint.model_validate_json(json_str)")
print("==========================")
json_str = pnt.model_dump_json()
pnt_from_json = GeoPoint.model_validate_json(json_str)
print(pnt_from_json)
print(type(pnt_from_json))

print("\nDate demo to show differences between model_dump* methods")
print("==========================")

class DateDemo(BaseModel):
    date: date

d = DateDemo(date=date.today())
print(f".model_dump()            {repr(d.model_dump())}")
print(f".model_dump_json()       {repr(d.model_dump_json())}")
print(f".model_dump(mode='json') {repr(d.model_dump(mode='json'))}")   




