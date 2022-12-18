"""Write a function (get_final_line) that takes a filename as an argument. The function should return that file's
final line on the screen """


# option 1 my solution
def get_final_line(file_name: str) -> None:
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


def get_final_line_2(file_name: str) -> None:
    final_line = ''
    for line in open(file_name):
        final_line = line
    return final_line


print(get_final_line_2('exercise_18_file.txt'))

# Beyond the excercise
"""Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace surrounded by whitespace) 
that contain only integers, and sum them"""
# I will use split() since it uses white space by default and is digit to confirm i is a digit
def find_integers_in_file(file_name: str) -> None:
    with open(file_name) as f:
        words = f.read().split()
        return sum(int(x) for x in words if x.isdigit())

print(find_integers_in_file('exercise_18_file.txt'))

# modification to include also numbers surrounded with ","
def find_integers_in_file_2(file_name: str) -> None:
    with open(file_name) as f:
        words = f.read().split()
        return sum(int(x.strip(",")) for x in words if x.strip(",").isdigit())

print(find_integers_in_file_2('exercise_18_file.txt'))
