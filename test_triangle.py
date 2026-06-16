"""Unit tests for the triangle module (pytest).

The tests are data-driven with @pytest.mark.parametrize (the pytest equivalent
of xUnit's [Theory] / [InlineData]) and exercise several capabilities of the
assert mechanism: truthiness, equality, ordering-independence, exceptions and
approximate float comparison.
"""
import pytest
from triangle import is_triangle, classify_triangle


# ---------------------------------------------------------------- valid cases
@pytest.mark.parametrize("a,b,c", [
    (3, 4, 5),        # classic right triangle
    (2, 2, 2),        # equilateral
    (5, 5, 8),        # isosceles
    (7, 10, 5),       # scalene, unsorted input
    (100, 100, 1),    # very thin but valid
    (0.5, 0.5, 0.5),  # floats
])
def test_valid_triangles(a, b, c):
    assert is_triangle(a, b, c) is True


# -------------------------------------------------------------- invalid cases
@pytest.mark.parametrize("a,b,c", [
    (1, 2, 3),        # degenerate: 1 + 2 == 3
    (1, 1, 2),        # degenerate
    (1, 2, 10),       # one side too long
    (10, 1, 2),       # same, unsorted
    (2, 10, 1),       # same, unsorted
])
def test_invalid_triangles(a, b, c):
    assert is_triangle(a, b, c) is False


# --------------------------------------------------- non-positive side lengths
@pytest.mark.parametrize("a,b,c", [
    (0, 4, 5),
    (-3, 4, 5),
    (3, 4, 0),
    (0, 0, 0),
])
def test_non_positive_sides_are_not_triangles(a, b, c):
    assert is_triangle(a, b, c) is False


# ----------------------------------------------- order of arguments is ignored
def test_argument_order_does_not_matter():
    assert is_triangle(3, 4, 5) == is_triangle(5, 4, 3) == is_triangle(4, 5, 3)


# ------------------------------------------------------- boundary / inequality
def test_degenerate_boundary_is_false():
    # exactly on the boundary a + b == c must be rejected
    assert is_triangle(2, 3, 5) is False


def test_just_above_boundary_is_true():
    assert is_triangle(2, 3, 4.999) is True


# ------------------------------------------------------------- float tolerance
def test_float_sides_close_to_boundary():
    # 0.1 + 0.2 + 0.2 -> longest 0.3 (?), check a robust valid float triangle
    assert is_triangle(0.1 + 0.2, 0.2, 0.2) is True


# ------------------------------------------------------------- classification
@pytest.mark.parametrize("a,b,c,expected", [
    (2, 2, 2, "equilateral"),
    (5, 5, 8, "isosceles"),
    (8, 5, 5, "isosceles"),
    (3, 4, 5, "scalene"),
    (1, 2, 10, "not a triangle"),
    (0, 0, 0, "not a triangle"),
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected


# ------------------------------------------------------------- error handling
@pytest.mark.parametrize("bad", ["3", None, True])
def test_non_numeric_raises_type_error(bad):
    with pytest.raises(TypeError):
        is_triangle(bad, 4, 5)
