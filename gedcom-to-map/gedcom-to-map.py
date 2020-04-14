import argparse

from creator.Creator import Creator
from gedcom.GedcomParser import GedcomParser
from kml.KmlExporter import KmlExporter


def gedcom_to_map(input_file, output_file, main_entity, max_missing=0, max_line_weight=1):
    humans = GedcomParser(input_file).create_humans()
    creator = Creator(humans, max_missing).create(main_entity)
    if main_entity not in humans:
        raise
    KmlExporter(output_file, max_line_weight).export(humans[main_entity].pos, creator)


class ArgParse(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="convert gedcom to kml file")
        self.add_argument('input_file', type=str)
        self.add_argument('output_file', type=str)
        self.add_argument('main_entity', type=str)
        self.add_argument('--max_missing', type=int, default=0, help="maximum generation missing (0 = no limit)")
        self.add_argument('--max_line_weight', type=int, default=5, help="line maximum weight")
        self.args = self.parse_args()


if __name__ == '__main__':
    arg_parse = ArgParse()
    gedcom_to_map(
        arg_parse.args.input_file,
        arg_parse.args.output_file,
        arg_parse.args.main_entity,
        max_missing=arg_parse.args.max_missing,
        max_line_weight=arg_parse.args.max_line_weight
    )
