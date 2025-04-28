import math
import pytest
from geometry import Triangle, Circle

@pytest.mark.parametrize("radius, expected_area", [
    (3, math.pi * 9),
    (5, math.pi * 25),
    (10, math.pi * 100),
])
def test_circle_area(radius, expected_area):
    circle = Circle(radius=radius)
    actual_area = circle.area()
    assert actual_area == expected_area


@pytest.mark.parametrize("a, b, c, expected_area", [
    (3, 4, 5, 6.0),
    (5, 12, 13, 30.0),
    (7, 24, 25, 84.0),
])
def test_triangle_area(a, b, c, expected_area):
    triangle = Triangle(a, b, c)
    actual_area = triangle.area()
    assert actual_area == expected_area


@pytest.mark.parametrize("a, b, c, is_right", [
    (3, 4, 5, True),
    (5, 12, 13, True),
    (7, 24, 25, True),
    (5, 6, 7, False),
    (8, 15, 17, True),
])
def test_triangle_is_right(a, b, c, is_right):
    triangle = Triangle(a, b, c)
    assert triangle.is_right_triangle() == is_right
