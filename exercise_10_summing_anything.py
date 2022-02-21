""""
This challange asks you to redefine the mysum() function we defined in chapter 1
such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operator (Thus, the function should
work with numbers, strings, lists, and tuples, but not sets and dicts)
"""
# my solution
def mysum(*args):
    result = args[0]
    if not args:
        return args
    else:
        for i in args[1:]:
            result += i
        return result
print(mysum([1,2,3,4,5], [50, 90], [0]))
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
