"""Triangle validation utilities.

The core function `is_triangle` checks whether three values can be used as the
side lengths of a valid (non-degenerate) triangle.

Rule (triangle inequality): three positive lengths form a triangle if and only
if the sum of the two shortest sides is strictly greater than the longest side.
A *degenerate* triangle, where a + b == c, is treated as NOT a triangle.
"""
from numbers import Real


def _validate(sides):
    for s in sides:
        # bool is a subclass of int - reject it explicitly
        if isinstance(s, bool) or not isinstance(s, Real):
            raise TypeError(f"side lengths must be real numbers, got {s!r}")


def is_triangle(a, b, c):
    """Return True if a, b, c can be the sides of a valid triangle.

    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(1, 1, 2)   # degenerate
    False
    >>> is_triangle(1, 2, 10)  # too long
    False
    """
    sides = (a, b, c)
    _validate(sides)
    if any(s <= 0 for s in sides):
        return False
    x, y, z = sorted(sides)          # z is the longest side
    return x + y > z


def classify_triangle(a, b, c):
    """Classify the triangle formed by a, b, c.

    Returns one of: 'equilateral', 'isosceles', 'scalene', 'not a triangle'.
    """
    if not is_triangle(a, b, c):
        return "not a triangle"
    distinct = len({a, b, c})
    if distinct == 1:
        return "equilateral"
    if distinct == 2:
        return "isosceles"
    return "scalene"


if __name__ == "__main__":
    for t in [(3, 4, 5), (2, 2, 2), (2, 2, 3), (1, 1, 2), (1, 2, 10), (0, 4, 5)]:
        print(t, "->", is_triangle(*t), "/", classify_triangle(*t))
