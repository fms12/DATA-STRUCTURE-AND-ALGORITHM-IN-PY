"""
function to check if two strings are
anagram or not
"""


def check(s1, s2):
    """
    Sort strings then check them
    """
    if sorted(s1) == sorted(s2):
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."
