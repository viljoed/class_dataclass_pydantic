"""Examples that will be run by *_demo.py for 
Python class, @dataclass, pydantic.models.BaseModel"""
def run(cls:type):
    longitude, latitude = -75.7552, 45.3484
    pnt = cls(longitude=longitude, latitude=latitude)
    print(pnt)

    longitude, latitude = 500, 200
    try:
        pnt = cls(longitude=longitude, latitude=latitude)
    except Exception as e:
        print(e)
        pnt = None