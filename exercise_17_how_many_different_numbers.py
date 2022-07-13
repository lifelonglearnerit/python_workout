"""
Assume that your Python program contains a list of integers.
We want to print the number of different integers contained within
that list. Thus, consider the following:
numbers = [1, 2, 3, 1, 2, 3, 4, 1]

Write a function, called how_many_different_numbers, that takes
a single list of integers and returns the number of different
integers it contains
"""
numbers = [1, 2, 3, 1, 2, 3, 4, 1]


def how_many_different_numbers(lst: list) -> int:
    different = set(lst)
    return len(different)

print(how_many_different_numbers(numbers))