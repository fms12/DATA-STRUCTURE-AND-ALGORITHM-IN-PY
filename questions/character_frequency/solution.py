"""
Question: Write a program that accepts a sentence (string)
and calculate the number of letters and digits.
"""


def solution(input_string: str):
    dict = {}

    for i in input_string:
        if i in dict:
            dict[i] += 1
            continue

        dict[i] = 1

    return dict
