import pytest

from sort import Stack
from sort import sort as sort_func


@pytest.mark.parametrize(
    "width,height,length,mass,expected",
    [
        (10, 10, 149, 19, Stack.STANDARD.upper()),
        (150, 10, 10, 10, Stack.SPECIAL.upper()),
        (10, 150, 10, 10, Stack.SPECIAL.upper()),
        (10, 10, 150, 10, Stack.SPECIAL.upper()),
        (10, 10, 10, 20, Stack.SPECIAL.upper()),
        (101, 101, 101, 19, Stack.SPECIAL.upper()),
        (101, 101, 101, 20, Stack.REJECTED.upper()),
    ],
)
def test_sort_valid_params(width, height, length, mass, expected):
    assert sort_func(width, height, length, mass) == expected


@pytest.mark.parametrize(
    "width,height,length,mass,expected",
    [
        (-1, 10, 10, 10, Stack.REJECTED.upper()),
        (10, -1, 10, 10, Stack.REJECTED.upper()),
        (10, 10, -1, 10, Stack.REJECTED.upper()),
        (10, 10, 10, -1, Stack.REJECTED.upper()),
    ],
)
def test_sort_invalid_params(width, height, length, mass, expected):
    assert sort_func(width, height, length, mass) == expected
