from __future__ import annotations

import argparse
from typing import Type, Dict

from creator.Creator import Creator
from exporter.GeoJsonExporter import GeoJsonExporter
from gedcom.GedcomParser import GedcomParser
from exporter.KmlExporter import KmlExporter


EXPORTERS: Dict[str, Type] = {
    "kml": KmlExporter,
    "geojson": GeoJsonExporter,
}


def gedcom_to_map(
    input_file: str,
    output_file: str,
    main_entity: str,
    output_format: str = "kml",
    max_missing: int = 0,
    max_line_weight: int = 1,
) -> None:
    if output_format not in EXPORTERS:
        raise ValueError(
            f"Unknown exporter '{output_format}'. Available: {', '.join(EXPORTERS)}"
        )
    humans = GedcomParser(input_file).create_humans()
    if main_entity not in humans:
        raise KeyError(f"Unknown main_entity '{main_entity}' in GEDCOM")
    lines = Creator(humans, max_missing).create(main_entity)
    exporter_cls = EXPORTERS[output_format]
    exporter = exporter_cls(output_file, max_line_weight)
    exporter.export(humans[main_entity].pos, lines)


class ArgParse(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="convert gedcom to a map file")
        self.add_argument(
            "input_file",
            type=str,
        )
        self.add_argument(
            "output_file",
            type=str,
        )
        self.add_argument(
            "main_entity",
            type=str,
        )
        self.add_argument(
            "--format",
            dest="output_format",
            choices=list(EXPORTERS.keys()),
            default="kml",
            help="output format",
        )
        self.add_argument(
            "--max_missing",
            type=int,
            default=0,
            help="maximum generation missing (0 = no limit)",
        )
        self.add_argument(
            "--max_line_weight",
            type=int,
            default=5,
            help="line maximum weight",
        )
        self.args = self.parse_args()


if __name__ == "__main__":
    arg_parse = ArgParse()
    gedcom_to_map(
        arg_parse.args.input_file,
        arg_parse.args.output_file,
        arg_parse.args.main_entity,
        output_format=arg_parse.args.output_format,
        max_missing=arg_parse.args.max_missing,
        max_line_weight=arg_parse.args.max_line_weight,
    )
