"""Write a function (get_final_line) that takes a filename as an argument. The function should return that file's
final line on the screen """


# option 1 my solution
def get_final_line(file_name: str) -> str:
    with open(file_name, 'r') as f:
        final_line = f.readlines()[-1]
    return final_line


print(get_final_line('exercise_18_file.txt'))

# option 2
# solution from the book
from io import StringIO

fake_file = StringIO("""
    This is very nice solution 
    Especially for testing 
    Because you can simulate file 
    Without touching file system.
    """)


def get_final_line_2(file_name: str) -> str:
    final_line = ''
    for line in open(file_name):
        final_line = line
    return final_line


print(get_final_line_2('exercise_18_file.txt'))

# Beyond the excercise
"""Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace surrounded by whitespace) 
that contain only integers, and sum them"""
# I will use split() since it uses white space by default and is digit to confirm i is a digit
def find_integers_in_file(file_name: str) -> int:
    with open(file_name) as f:
        words = f.read().split()
        return sum(int(x) for x in words if x.isdigit())

print(find_integers_in_file('exercise_18_file.txt'))

# modification to include also numbers surrounded with ","
def find_integers_in_file_2(file_name: str) -> int:
    with open(file_name) as f:
        words = f.read().split()
        return sum(int(x.strip(",")) for x in words if x.strip(",").isdigit())

print(find_integers_in_file_2('exercise_18_file.txt'))



"""Create a text file containing two tab-separated columns, 
with each column containing a number. Then use Python to read 
through the file you've created. For each line, multiply each first number
by the second, and then sum the results from all the lines. Ignore any line that 
doesn't contain two numeric columns
"""
def create_file(file_name: str) -> int:
    with open(file_name, 'w') as f:
        f.write('  non  numeric\n')
        for i in range(10):
            f.write(f'  {i}  {i+3}\n')


def sum_columns(file_name: str) -> None:
    sum_result = 0
    with open(file_name) as f:
        for line in f.readlines():
            numbers = line.split()
            print(line.split())
            if numbers[0].isdigit() and numbers[1].isdigit():
                sum_result += int(numbers[0]) * int(numbers[1])
        return sum_result

def test():
    create_file('test1.txt')
    print(sum_columns('test1.txt'))

test()

# option 2 with generator

def sum_columns_2(file_name: str) -> int:
    return sum(
        int(x.split()[0]) * int(x.split()[1])
        for x in open(file_name).readlines()
        if (x.split()[0].isdigit() and x.split()[1].isdigit())
    )

print(sum_columns_2('test1.txt'))