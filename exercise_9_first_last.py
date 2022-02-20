"""
Write a function, firstlast(), that takes a sequence (string, list or tuple)
and returns the first and last elements of that sequence, in a two-element sequence
of the same type. So for firstlast('abc') will return the string 'ac', while
firstlast([1, 2, 3, 4]) will return the list [1, 4]
"""


# my solution without reading any farther explanations:
def firstlast(sequence):
    if type(sequence) == str:
        return ''.join((sequence[0], sequence[-1]))
    else:
        return type(sequence)((sequence[0], sequence[-1]))


print(firstlast([1, 2, 3, 4]))
print(firstlast('abc'))
print(firstlast((1, 3, 4, 5)))


# book solution
def firstlast_book(sequence):
    return sequence[:1] + sequence[-1:]


print(firstlast_book('abcd'))
print(firstlast_book((1, 3, 4, 5)))

"""
Reflection: with each exercise I learn a lot about thinking in more pythonic way
here the most important takeaway: if you retrieve slice from an object x, you'll 
get new object of the same type as x. But if you retrieve individual element 
(as I did in my solution) you'll get whatever was stored in. 
"""

# Beyond the exercise
"""
write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of the 
odd-indexed numbers. So callin the function as even_odd_sums([10,20,30,40,50,60])
you'll get back [90, 120]
"""


def even_odd_sums(sequence):
    even_sum = sum([x for i, x in enumerate(sequence) if i % 2 == 0])
    odd_sum = sum([y for i, y in enumerate(sequence) if i % 2 != 0])
    return type(sequence)((even_sum, odd_sum))


print(even_odd_sums([10, 20, 30, 40, 50, 60]))


def even_odd_sums_2(sequence):
    return type(sequence)((sum(sequence[0::2]), sum(sequence[1::2])))


print(even_odd_sums_2([10, 20, 30, 40, 50, 60]))

"""
Write a function that takes a list or tuple of numbers. Return result of alternately 
adding and subtracting numbers from each other. So calling the function as
plus_minus([10, 20, 30, 40, 50, 60,]) you'll get back result of:
10+20-30+40-50+60 or 50
"""


def plus_minus(sequence):
    total = sequence[0]
    flag = True
    for number in sequence[1:]:
        if flag:
            total += number
            flag = False
        elif not flag:
            total -= number
            flag = True
    return total


print(plus_minus([10, 20, 30, 40, 50, 60, ]))

"""
Write a function that partly emulates the built-in zip function, taking any number 
of iterables and returning a list of tuples. Each tuple will contain one element 
from each of the iterables passed to the function. Thus, if I call myzip([10, 20, 30], 'abc'), 
the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. You can return a list (not an iterator) and 
assume that all of the iterables are of the same length.
"""
def myzip(*iterables):
    pass
# this one I need to solve later
