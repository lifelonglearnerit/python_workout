"""
Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return
the string that contains the greatest number of repeated letters. In other words:
- for each word, find the letter that appears the most times
- find the word whose most-repeated letter appears more than any other
"""
# my naive first solution
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

# ----------------METHODS TO BE USED---------------------
# Counter from collections module - it inherits from dict
# most_common - returns a list of n most common elements
# and their counts from the most common to leas
# -------------------------------------------------------

from collections import Counter

print(Counter(WORDS[3]))
print(Counter(WORDS[3]).most_common())


# my solution based on info from book
def most_repeating_word(string_list: list[str]) -> str:
    return max(string_list,
               key=lambda word: Counter(word).most_common(1)[0][1])


print(most_repeating_word(WORDS))

# solution from the book
import operator


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max (words,
                key=most_repeating_letter_count)

print(most_repeating_word(WORDS))