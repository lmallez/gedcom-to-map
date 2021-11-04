from typing import Dict

from models.Color import Color
from models.Human import Human
from models.Line import Line
from models.Pos import Pos
from models.Rainbow import Rainbow


class Creator:
    def __init__(self, humans: Dict[str, Human], max_missing=0):
        self.humans = humans
        self.rainbow = Rainbow()
        self.max_missing = max_missing

    def line(self, pos: Pos, current: Human, branch, prof, miss, path="") -> [Line]:
        if current.pos:
            print("{:8} {:8} {:2} {:.10f} {} {:20}".format(path, branch, prof, (branch+1/2)/(2**prof), self.rainbow.get((branch+1/2)/(2**prof)).to_hexa(), current.name))
            line = Line("{:8} {}".format(path, current.name), pos, current.pos, self.rainbow.get((branch+1/2)/(2**prof)), prof)
            return self.link(current.pos, current, branch, prof, 0, path) + [line]
        else:
            if self.max_missing != 0 and miss >= self.max_missing:
                return []
            return self.link(pos, current, branch, prof, miss+1, path)

    def link(self, pos: Pos, current: Human, branch=0, prof=0, miss=0, path="") -> [Line]:
        return (self.line(pos, self.humans[current.father], branch*2, prof+1, miss, path + "0") if current.father else []) \
               + (self.line(pos, self.humans[current.mother], branch*2+1, prof+1, miss, path + "1") if current.mother else [])

    def create(self, main_id: str):
        if main_id not in self.humans.keys():
            raise
        current = self.humans[main_id]
        return self.link(current.pos, current)
