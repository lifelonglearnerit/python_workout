"""
Write a Python function (pig_latin) that takes a string as input assumed to be
an English word. The function should return the translation of this word into
Pig Latin. You may assume that the word contains no capital letters or punctuation.
Rules:
if word begins with vowel: a, e, i o, u; add way at the end of the word
if word begins with any other letter move fist letter to the end of the word
and add 'ay': computer >> omputercay
"""
# my solution
def pig_latin():
    word = input('Write the word: ')
    if word[0] in 'aeiou':
        print(f'{word}way')
    else:
        print(word[1:]+word[0] + 'ay')
pig_latin()

# solution from book<
def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
print(pig_latin('python'))