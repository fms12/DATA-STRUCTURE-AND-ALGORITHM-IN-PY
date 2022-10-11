from .solution import solution
import pytest


@pytest.mark.parametrize("input_string, expected", [
    (
        "hello world! 123",
        {
            "h": 1, "e": 1, "l": 3, "o": 2, " ": 2,
            "w": 1, "r": 1, "d": 1, "!": 1, "1": 1,
            "2": 1, "3": 1
        }
    ),
    ("", {}),
    ("a", {"a": 1}),
    ("aa", {"a": 2}),
    ("aaa", {"a": 3}),
    ("aaaa", {"a": 4}),
])
def test_character_frequency(input_string, expected):
    result = solution(input_string)
    assert(result == expected)
