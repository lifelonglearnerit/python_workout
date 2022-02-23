""""
This challange asks you to redefine the mysum() function we defined in chapter 1
such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operator (Thus, the function should
work with numbers, strings, lists, and tuples, but not sets and dicts)
"""


# my solution
def mysum(*args):
    if not args:
        return args
    else:
        result = args[0]
        for i in args[1:]:
            result += i
        return result


print(mysum([1, 2, 3, 4, 5], [50, 90], [0]))
print(mysum())

# Beyond the exercise:
""""
Write a function, mysum_bigger_than(), that works the same as mysum, except that 
it takes a first argument that precedes *args. That argument indicates the threshold 
for including an argument in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) 
would return 50 - because 5 and 6 aren't greater than 10. This function should simlilarly 
work with any type and assumes that all of the arguments are of the same type. Note that 
> and < work on many different types in Python,not just on number; with strings, lists, and 
tuples, it refers to their sort order.
"""


def mysum_bigger_than(x, *args):
    print('1:', args)
    if not args:
        return args
    else:
        bigger_than = [item for item in args if item > x]
        result = bigger_than[0]
        for i in bigger_than[1:]:
            result += i
        return result


print(mysum_bigger_than(10, 5, 20, 30, 6))
print(mysum_bigger_than('k', 'I', 'am', 'interested', 'in', 'learning', 'Python'))

"""
Write a function, sum_numeric, that takes any number of arguments. If the argument is or can be 
turned int an integer, then it should be added to the total. Arguments that can't be handled as 
integers should be ignored. The result is the sum of the numbers. 
Thus, sum_numeric(10, 20, 'a', '30', 'bcd') would return 60. 
"""


def sum_numeric(*args):
    num_sum = []
    for item in args:
        try:
            num_sum.append(int(item))
        except ValueError:
            continue
    return sum(num_sum)


print(sum_numeric(10, 20, 'a', '30', 'bcd'))


