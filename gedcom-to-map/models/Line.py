from models.Color import Color
from models.Pos import Pos


class Line:
    def __init__(self, name: str, a: Pos, b: Pos, color: Color, prof: int):
        self.name = name
        self.a = a
        self.b = b
        self.color = color
        self.prof = prof

    def __repr__(self):
        return "( {}, {} )".format(self.a, self.b)