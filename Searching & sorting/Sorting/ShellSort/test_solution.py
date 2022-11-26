from .solution import shellSort
import pytest

print(pytest)

numbers = [9, 8, 3, 7, 5, 6, 4, 1]
Ans = sorted(numbers)


def test_sort_Asce():
    shellSort(numbers,len(numbers))
    assert numbers == Ans
