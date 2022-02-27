"""
Let's assume you have phone book data in a list of dicts, as follows:
PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'murderer@kreml.ru'}]
Write a function, alphabetize_names, that assumes the existence of a PEOPLE constant defined.
The function should return the list of dicts, but sored by last name and then by first name.

"""
import operator

PEOPLE = [{'first': 'Tomasz', 'last': 'Waszczewski', 'email': 'lifelonglearnerit@gmail.com'},
          {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'murderer@kreml.ru'}
          ]


# ---------------------------------------SORTED--------------------------------------------
# value passed to parameter key in sorted must be a function that takes a single argument
# the function will be invoked once per element, and function's return value will will be
# used to sort the values
# -----------------------------------------------------------------------------------------

def alphabetize_my(dicts):
    return sorted(dicts, key=lambda x: [x['last'], x['first']])


print(alphabetize_my(PEOPLE))


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))


# beyond the exercise
"""
Given a sequence of positive and negative numbers, sort them by absolute value
"""


def abs_sort(*sequence):
    absolute = []
    if not sequence:
        return sequence
    elif len(sequence) == 1:
        for seq in sequence:
            for item in seq:
                absolute.append(abs(float(item)))
        return f'list or tuple {sorted(absolute)}'
    else:
        return type(sequence)(sorted([abs(float(x)) for x in sequence]))


print(abs_sort(-55, 2, 77, -0.1))            # integers
print(abs_sort('-55', '2', '77', '-0.1'))    # strings
print(abs_sort(['-55', '2', '77', '-0.1']))  # list
print(abs_sort(('-55', '2', '77', '-0.1')))  # tuple

"""
Given a list of strings, sort them according to how many vowels they contain
"""
def vowel_sort(string_list: list[str]) -> list[str]:
    return sorted(string_list,
                  key=lambda word: sum(vowel in 'aeiou' for vowel in word))

print(vowel_sort(['uoi', 'u', 'uoiea', 'uo',  'uoie' ]))



