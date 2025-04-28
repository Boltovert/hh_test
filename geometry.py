import math
from abc import ABC, abstractmethod


class Geometry(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Geometry):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        if self.radius <= 0:
            raise ValueError("your value is zero or less")
        return math.pi * self.radius ** 2

class Triangle(Geometry):
    def __init__(
        self,
        a: float,
        b: float,
        c: float
    ):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        sides = sorted([self.a, self.b, self.c])
        if any(side <= 0 for side in sides):
            raise ValueError("all sides must be greater than 0")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("no valid sides for triangle")
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        if (sides[0] ** 2) * (sides[1] ** 2) == (sides[2]**2):
            return True
