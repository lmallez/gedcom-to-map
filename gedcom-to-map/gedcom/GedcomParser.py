from typing import Dict

from ged4py import GedcomReader
from ged4py.model import Record

from models.Human import Human
from models.Pos import Pos


class GedcomParser:
    def __init__(self, file_name):
        self.file_path = file_name

    @staticmethod
    def __create_human(record: Record) -> Human:
        human = Human(record.xref_id)
        name: Record = record.sub_tag("NAME")
        if name:
            human.name = "{} {}".format(name.value[0], name.value[1])
        birt = record.sub_tag("BIRT")
        if birt:
            plac = birt.sub_tag("PLAC")
            if plac:
                map = plac.sub_tag("MAP")
                if map:
                    lat = map.sub_tag("LATI")
                    lon = map.sub_tag("LONG")
                    if lat and lon:
                        human.pos = Pos(
                            (
                                lat.value[1:]
                                if lat.value[0] == "N"
                                else "-{}".format(lat.value[1:])
                            ),
                            (
                                lon.value[1:]
                                if lon.value[0] == "E"
                                else "-{}".format(lon.value[1:])
                            ),
                        )
        return human

    @staticmethod
    def __create_humans(records0) -> Dict[str, Human]:
        humans = dict()
        for record in records0("INDI"):
            humans[record.xref_id] = GedcomParser.__create_human(record)
        for record in records0("FAM"):
            husband = record.sub_tag("HUSB")
            wife = record.sub_tag("WIFE")
            for chil in record.sub_tags("CHIL"):
                if chil.xref_id not in humans.keys():
                    continue
                if husband:
                    humans[chil.xref_id].father = husband.xref_id
                if wife:
                    humans[chil.xref_id].mother = wife.xref_id
        return humans

    def create_humans(self) -> Dict[str, Human]:
        with GedcomReader(self.file_path) as parser:
            return self.__create_humans(parser.records0)
