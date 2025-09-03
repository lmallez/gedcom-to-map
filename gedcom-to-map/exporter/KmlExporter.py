from __future__ import annotations

import math
from typing import List

import simplekml
from models.Line import Line
from models.Pos import Pos


class KmlExporter:
    def __init__(self, file_name: str, max_line_weight: int = 1):
        self.file_name = file_name
        self.max_line_weight = max_line_weight
        self._decay_base = math.exp(0.5)

    def _width_for_prof(self, prof: int) -> int:
        return max(int(self.max_line_weight / (self._decay_base ** prof)), 1)

    def export(self, main: Pos, lines: List[Line]) -> None:
        kml = simplekml.Kml()
        kml.newpoint(coords=[(main.lon, main.lat)])
        for line in lines:
            kml_line = kml.newlinestring(
                name=line.name,
                coords=[(line.a.lon, line.a.lat), (line.b.lon, line.b.lat)],
            )
            kml_line.linestyle.color = line.color.to_hexa()
            kml_line.linestyle.width = self._width_for_prof(line.prof)
        kml.save(self.file_name)