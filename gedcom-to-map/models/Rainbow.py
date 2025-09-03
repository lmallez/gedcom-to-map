from __future__ import annotations

from dataclasses import dataclass

from models.Color import Color


def merge_color(color_a: Color, color_b: Color, coef: float) -> Color:
    return Color(
        int(color_a.r * (1 - coef) + color_b.r * coef),
        int(color_a.g * (1 - coef) + color_b.g * coef),
        int(color_a.b * (1 - coef) + color_b.b * coef),
    )


@dataclass
class Tint:
    x: int
    y: int
    min: Color
    max: Color

    def is_inside(self, val: int) -> bool:
        return self.x <= val < self.y

    def get_color(self, val: int) -> Color:
        diff = (val - self.x) / (self.y - self.x)
        return merge_color(self.min, self.max, diff)


class Rainbow:
    def __init__(self):
        self.steps = [
            Color(255, 0, 127),
            Color(255, 0, 0),
            Color(255, 127, 0),
            Color(255, 255, 0),
            Color(127, 255, 0),
            Color(0, 255, 0),
            Color(0, 255, 127),
            Color(0, 255, 255),
            Color(0, 127, 255),
            Color(0, 0, 255),
        ]

    def get(self, v: float) -> Color:
        if not (0 <= v < 1):
            raise ValueError("v must be in [0, 1)")
        n = len(self.steps) - 1
        step = int(v * n)
        pos = (v * n) - step
        return merge_color(self.steps[step], self.steps[step + 1], pos)
