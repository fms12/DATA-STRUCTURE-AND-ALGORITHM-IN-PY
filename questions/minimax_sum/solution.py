

import string


def solution(string_iter: str):
    """
    The sum is sum(iterable, start) iterable can
    be anything list , tuples or dictionaries ,
    but most importantly it should be numbers.
    """
    nums = [int(x) for x in string_iter.strip().split(' ')]
    return (sum(nums) - max(nums), sum(nums) - min(nums))
