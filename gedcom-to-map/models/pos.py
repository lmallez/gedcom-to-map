from dataclasses import dataclass


@dataclass
class Pos:
    lat: float
    lon: float

    def __repr__(self):
        return "{},{}".format(self.lon, self.lat)
