# write a mysum function that does the same thing as the built-in sum function
# instead of taking single sequence as parameter it should take a variable number of arguments

# my solution
def mysum(*args):
    sum = 0
    for number in args:
        sum += int(number)
    return sum


print(mysum(10, 20, 30, 40, 5))


# solution from book
def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


print(mysum(10, 20, 30, 40))


# beyond exercise
# write the function that takes list of numbers and returns arithmetic mean
def mymean(num_list: list) -> float:
    sum = 0
    for number in num_list:
        sum += int(number)
    return sum / len(num_list)


print(mymean([1, 2, 3]))


# write function that takes list of strings and returns tuple containing three integers
# representing length of the shortest word, length of the longest word, and avg word length
def strings(str_list: list) -> tuple:
    length = []
    for word in str_list:
        length.append(len(word))
    return (min(length), max(length), int(mymean(length)))


print(strings(['t', 'tw', 'str']))


# write a function that takes a list of Python objects.
# Sum the objects that either are integers or can be turned into integers, ignoring the others
def objects_sum(objects: list) -> int:
    obj_sum = 0
    for object in objects:
        obj_sum += int(object)
    return obj_sum


print(objects_sum(['1', '2', 3.0]))
