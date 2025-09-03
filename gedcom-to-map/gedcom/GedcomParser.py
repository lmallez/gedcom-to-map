from __future__ import annotations

from typing import Dict

from ged4py import GedcomReader
from ged4py.model import Record

from models.Human import Human
from models.Pos import Pos


class GedcomParser:
    def __init__(self, file_name: str):
        self.file_path = file_name

    @staticmethod
    def _signed(coord: str) -> float:
        # coord like "N50.1234" or "W003.4567"
        head, tail = coord[0], coord[1:]
        if head in ("N", "E"):
            return float(tail)
        return float("-{tail}")

    @staticmethod
    def _create_human(record: Record) -> Human:
        human = Human(record.xref_id)

        name_rec: Record | None = record.sub_tag("NAME")
        if name_rec:
            # Keep exact order as before: given then family
            human.name = f"{name_rec.value[0]} {name_rec.value[1]}"

        birt = record.sub_tag("BIRT")
        if birt:
            plac = birt.sub_tag("PLAC")
            if plac:
                map_rec = plac.sub_tag("MAP")
                if map_rec:
                    lat = map_rec.sub_tag("LATI")
                    lon = map_rec.sub_tag("LONG")
                    if lat and lon:
                        human.pos = Pos(
                            GedcomParser._signed(lat.value),
                            GedcomParser._signed(lon.value),
                        )
        return human

    @staticmethod
    def _create_humans(records0) -> Dict[str, Human]:
        humans: Dict[str, Human] = {}

        for rec in records0("INDI"):
            humans[rec.xref_id] = GedcomParser._create_human(rec)

        for fam in records0("FAM"):
            husband = fam.sub_tag("HUSB")
            wife = fam.sub_tag("WIFE")
            for chil in fam.sub_tags("CHIL"):
                cid = chil.xref_id
                if cid not in humans:
                    continue
                child = humans[cid]
                if husband:
                    child.father_id = husband.xref_id
                if wife:
                    child.mother_id = wife.xref_id
        return humans

    def create_humans(self) -> Dict[str, Human]:
        with GedcomReader(self.file_path) as parser:
            return self._create_humans(parser.records0)
