"""
Test the check anagram function
"""


from .solutions import check
import pytest


@pytest.mark.parametrize("s1, s2, expected", [
    ("listen", "silent", "The strings are anagrams."),
    ("earth", "heart", "The strings are anagrams."),
    ("python", "typhon", "The strings are anagrams."),
    ("python", "typho", "The strings aren't anagrams."),
    ("python", "typhons", "The strings aren't anagrams."),
    ("python", "typhon", "The strings are anagrams."),
])
def test_check(s1, s2, expected):
    assert check(s1, s2) == expected
