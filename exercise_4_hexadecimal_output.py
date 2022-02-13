"""
you need to write function (hex_output) that takes a hex number and returns decimal equivalent
--- from uni classes :) ---
hex |0|1|2|3|4|5|6|7|8|9|A |B |C |D |E |F |
dec |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|
example: C9 -- from classes :)
9 = 9 * (16 ** 0) = 9
C = 12 * (16 ** 1) = 192
192 + 9 = 201
"""
# my solution
def hex_output(hex_num: str) -> int:
    hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3,
               '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    for i, v, in enumerate(reversed(hex_num)):
        decimal += hex_dec[v] * (16 ** i)

    return decimal


hex_num = input('Please enter number in Hexadecimal: ')
print(f'{hex_num} is {hex_output(hex_num)} in Decimal')


# solution from book
# it seems that I did not understood the task :)
# I could use built-in int() and define the base
# main take away is read everything ;)

def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)
hex_output()