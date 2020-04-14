import math

import simplekml as simplekml
from models.Line import Line
from models.Pos import Pos


class KmlExporter:
    def __init__(self, file_name, max_line_weight=1):
        self.file_name = file_name
        self.max_line_weight = max_line_weight

    def export(self, main: Pos, lines: [Line]):
        kml = simplekml.Kml()
        kml.newpoint(coords=[
            (main.lon, main.lat)
        ])
        for line in lines:
            kml_line = kml.newlinestring(name=line.name, coords=[
                (line.a.lon, line.a.lat), (line.b.lon, line.b.lat)
            ])
            kml_line.linestyle.color = line.color.to_hexa()
            kml_line.linestyle.width = max(
                int(self.max_line_weight/math.exp(0.5*line.prof)),
                1
            )
        kml.save(self.file_name)
