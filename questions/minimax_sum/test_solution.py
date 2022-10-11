
import pytest
from .solution import solution


@pytest.mark.parametrize("test_input,expected", [
    ("1 2 3 4 5", (10, 14)),
    ("1 2 3 4 5 6", (15, 20)),
    ("1 2 3 4 5 6 7", (21, 27)),
    ("1 2 3 4 5 6 7 8", (28, 35)),
    ("1 2 3 4 5 6 7 8 9", (36, 44)),
    ("1 2 3 4 5 6 7 8 9 10", (45, 54)),
    ("1 2 3 4 5 6 7 8 9 10 11", (55, 65)),
    ("1 2 3 4 5 6 7 8 9 10 11 12", (66, 77)),
])
def test_solution(test_input, expected):
    assert solution(test_input) == expected
