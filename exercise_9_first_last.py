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