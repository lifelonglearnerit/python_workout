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
