class Pos:
    def __init__(self, lon, lat):
        self.lat = lon
        self.lon = lat

    def __repr__(self):
        return "{},{}".format(self.lon, self.lat)