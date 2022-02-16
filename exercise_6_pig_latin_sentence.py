"""
Write a function called pl_sentence that takes a string containing several words, separated
by spaces. (To make things easier, we won't actually ask for a real sentence. More specifically,
there will be no capital letters or punctuation)
"""


# my solution
def pl_sentence(sentence):
    sentence = sentence.split()
    for index, word in enumerate(sentence):
        if word[0] in 'aeiou':
            sentence[index] = f'{word}way'
        else:
            sentence[index] = f'{word[1:]}{word[0]}ay'
    return ' '.join(sentence)


print(pl_sentence('this is a test translation'))


# solution from the book
def pl_sentence_book(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)


print(pl_sentence_book('this is test'))

# Beyond the exercise - additional modifications suggested by author:
"""
Take a text file, creating and printing a nonsensical sentence from the nth 
word on each of the first 10 lines, where n is the line number 
"""
def nonsensical():
    with open('exercise_6_beyond.txt') as f:
        lines = f.readlines()
    first_10 = [line.split() for number, line in enumerate(lines) if number < 10]
    nonsensical_sentence = [word[9] for word in first_10 if len(word) >= 10]
    print(' '.join(nonsensical_sentence))

nonsensical()

"""
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a 
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'] 
['abc def ghi', 
'jkl mno pqr', 
'stu vwx yz']
Output: 
['abc jkl stu', 
'def mno vwx', 
'ghi pqr yz'] 
"""


def transpose(strings: list[str]) -> list[str]:
    index = 0
    transposed = []
    for i, _ in enumerate(strings):
        for row in strings:
            transposed.append(row.split()[index])
        index += 1
    for i in range(0, len(transposed), 3):
        transposed.append(' '.join(transposed[i:i+3]))
    return transposed[-3:]


print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))



