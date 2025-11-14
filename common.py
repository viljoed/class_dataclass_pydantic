def run(cls):
    longitude, latitude = -75.7552, 45.3484
    pnt = cls(longitude=longitude, latitude=latitude)
    print(pnt)

    longitude, latitude = 500, 200
    try:
        pnt = cls(longitude=longitude, latitude=latitude)
    except Exception as e:
        print(e)
        pnt = None