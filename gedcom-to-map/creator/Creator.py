from __future__ import annotations

from typing import Dict, List

from models.Human import Human
from models.Line import Line
from models.Pos import Pos
from models.Rainbow import Rainbow

space = 2.5
delta = 1.5


class Creator:
    def __init__(self, humans: Dict[str, Human], max_missing: int = 0):
        self.humans = humans
        self.rainbow = Rainbow()
        self.max_missing = max_missing

    def _append_line_and_recurse(
        self,
        acc: List[Line],
        pos: Pos,
        current: Human,
        branch: float,
        prof: int,
        miss: int,
        path: str,
    ) -> None:
        if current.pos:
            color_val = (branch + delta / 2) / (space**prof)
            color_obj = self.rainbow.get(color_val)

            print(
                "{:8} {:8} {:2} {:.10f} {} {:20}".format(
                    path,
                    branch,
                    prof,
                    color_val,
                    color_obj.to_hexa(),
                    current.name,
                )
            )

            self._link(acc, current.pos, current, branch, prof, 0, path)

            acc.append(
                Line(
                    f"{path:8} {current.name}",
                    pos,
                    current.pos,
                    color_obj,
                    prof,
                )
            )
            return

        if self.max_missing != 0 and miss >= self.max_missing:
            return

        self._link(acc, pos, current, branch, prof, miss + 1, path)

    def _link(
        self,
        acc: List[Line],
        pos: Pos,
        current: Human,
        branch: float = 0.0,
        prof: int = 0,
        miss: int = 0,
        path: str = "",
    ) -> None:
        if current.father_id:
            father = self.humans[current.father_id]
            self._append_line_and_recurse(
                acc,
                pos,
                father,
                branch * space,
                prof + 1,
                miss,
                path + "0",
            )

        if current.mother_id:
            mother = self.humans[current.mother_id]
            self._append_line_and_recurse(
                acc,
                pos,
                mother,
                branch * space + delta,
                prof + 1,
                miss,
                path + "1",
            )

    def create(self, main_id: str) -> List[Line]:
        if main_id not in self.humans:
            raise KeyError(f"Unknown human id: {main_id}")
        current = self.humans[main_id]
        acc: List[Line] = []
        self._link(acc, current.pos, current)
        return acc
