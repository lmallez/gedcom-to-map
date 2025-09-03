from dataclasses import dataclass

from models.Pos import Pos


@dataclass
class Human:
    xref_id: str
    name: str = None
    father_id: str = None
    mother_id: str = None
    pos: Pos = None

    def __repr__(self):
        return "[ {} : {} - {} {} - {} ]".format(
            self.xref_id, self.name, self.father_id, self.mother_id, self.pos
        )
