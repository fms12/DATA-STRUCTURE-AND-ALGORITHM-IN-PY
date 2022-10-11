from .solution import shuffle

"""
Test the shuffle function
"""


def test_shuffle():
    result = shuffle("python")
    assert(result != "python")
    assert(len(result) == len("python"))
