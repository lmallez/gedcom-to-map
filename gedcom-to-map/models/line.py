from dataclasses import dataclass

from models.color import Color
from models.pos import Pos


@dataclass
class Line:
    name: str
    a: Pos
    b: Pos
    color: Color
    prof: int

    def __repr__(self):
        return "( {}, {} )".format(self.a, self.b)
