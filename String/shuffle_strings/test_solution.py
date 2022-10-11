"""
Test the shuffle function
"""

from .solution import shuffle


def test_shuffle():
    result = shuffle("python")
    assert(result != "python")
    assert(len(result) == len("python"))
