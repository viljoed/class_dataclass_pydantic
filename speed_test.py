from geo_point_class import GeoPoint as gpc
from geo_point_dataclass import GeoPoint as gpd
from geo_point_pydantic import GeoPoint as gpp
import time

N = 100000
def instantiation_speed(label, fn):
    start = time.perf_counter()
    for _ in range(N):
        try:
            fn()
        except ValueError:
            pass
    end = time.perf_counter()
    print(f"{label:20} {end - start:.3f} sec")

lt, lng = 60, -75
instantiation_speed("Class", lambda: gpc(longitude=lng, latitude=lt))
instantiation_speed("Dataclass", lambda: gpc(longitude=lng, latitude=lt))
instantiation_speed("Pydantic v2", lambda: gpp(longitude=lng, latitude=lt))

lt, lng = 200, 900

instantiation_speed("Class", lambda: gpc(longitude=lng, latitude=lt))
instantiation_speed("Dataclass", lambda: gpc(longitude=lng, latitude=lt))
instantiation_speed("Pydantic v2", lambda: gpp(longitude=lng, latitude=lt))

