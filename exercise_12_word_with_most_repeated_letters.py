"""
Write a function, most_repeating_word, that takes a sequence of strings as input. The function should return
the string that contains the greatest number of repeated letters. In other words:
- for each word, find the letter that appears the most times
- find the word whose most-repeated letter appears more than any other
"""
# my naive first solution
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example', 'aeiioouu']

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

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max (words,
                key=most_repeating_letter_count)

print(most_repeating_word(WORDS))

# beyond the exercise
"""
Instead finding the word with the greatest number of repeated letters, 
find the word with the greatest number of repeated vowels 
"""

def repeated_vowels(word: list[str]) -> str:
    return [Counter(x) for x in word]
"""[Counter({'t': 1, 'h': 1, 'i': 1, 's': 1}), 
    Counter({'i': 1, 's': 1}), 
    Counter({'a': 1, 'n': 1}), 
    Counter({'e': 3, 'l': 1, 'm': 1, 'n': 1, 't': 1, 'a': 1, 'r': 1, 'y': 1}), 
    Counter({'t': 2, 'e': 1, 's': 1}), 
    Counter({'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}), 
    Counter({'i': 2, 'o': 2, 'u': 2, 'a': 1, 'e': 1})]"""

print('VOWEL', repeated_vowels(WORDS))
rep_vow = {}
for i, v in enumerate(repeated_vowels(WORDS)):
    for vow in 'aeioe':
        rep_vow[i] = v[vow]
        print(i, v[vow])
    print(rep_vow)