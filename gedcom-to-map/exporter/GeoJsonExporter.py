from __future__ import annotations

import json
from typing import List, Dict, Any

from models.Line import Line
from models.Pos import Pos


class GeoJsonExporter:
    def __init__(self, file_name: str, max_line_weight: int = 1):
        self.file_name = file_name
        self.max_line_weight = max_line_weight

    def export(self, main: Pos, lines: List[Line]) -> None:
        features: List[Dict[str, Any]] = [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [main.lon, main.lat],
            },
            "properties": {"name": "main"},
        }]

        for line in lines:
            features.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                            [line.a.lon, line.a.lat],
                            [line.b.lon, line.b.lat],
                        ],
                    },
                    "properties": {
                        "name": line.name,
                        "prof": line.prof,
                        "color": line.color.to_hexa(),
                        "width": max(
                            int(self.max_line_weight), 1
                        ),
                    },
                }
            )

        fc = {"type": "FeatureCollection", "features": features}
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(fc, f, ensure_ascii=False, separators=(",", ":"))
