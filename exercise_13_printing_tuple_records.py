"""
Write a Python function, format_sort_records(), that takes the PEOPLE list
and returns a formatted string that looks like the following:
Trump  Donald     7.85
Putin  Murderer   3.63
Xi     Jinping    10.60
"""
import operator

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


# solution from the book
def format_sort_records(list_of_tuples: list[tuple]) -> list[str]:
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples,
                         key=operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    return output


print('\n'.join(format_sort_records(PEOPLE)))
