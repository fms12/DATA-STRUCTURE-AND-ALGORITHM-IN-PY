"""
Question: Write a program that accepts a sentence (string)
and calculate the number of letters and digits.
"""


def solution(input_string: str):
    dictionary = {}

    for i in input_string:
        if i in dictionary:
            dictionary[i] += 1
            continue

        dictionary[i] = 1

    return dictionary
