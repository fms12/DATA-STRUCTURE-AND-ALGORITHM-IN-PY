from .solution import spiralOrder


def test_spiral_matrix():
    result = spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert(result == [1, 2, 3, 6, 9, 8, 7, 4, 5])
