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
