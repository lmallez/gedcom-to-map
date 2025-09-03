from dataclasses import dataclass


@dataclass
class Color:
    r: int = 255
    g: int = 0
    b: int = 0
    a: int = 255

    def to_hexa(self) -> str:
        return "{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

    def __repr__(self):
        return "({:3}, {:3}, {:3}, {:3})".format(self.r, self.g, self.b, self.a)
