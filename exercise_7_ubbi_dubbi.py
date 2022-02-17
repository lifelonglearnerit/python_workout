"""
For this exercise you'll write function (ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the word's translation
into Ubbi Dubbi (each vowel is prefaced with 'ub'. So if the function is
called with 'octopus', the function will return the string 'uboctubopubus'.
And if the user passes the argument 'elephant', you'll output 'ubelubephubant'.
"""
# my solution
def ubbi_dubbi(word: str) -> str:
    word = [letter for letter in word]
    vowel_index = [index for index, vowel in enumerate(word) if vowel in ['a', 'e', 'i', 'o', 'u']]
    for idx in vowel_index:
        word[idx] = f'ub{word[idx]}'
    return ''.join(word)


print(ubbi_dubbi('octopus'))
print(ubbi_dubbi('elephant'))


# solution from the book
def ubbi_dubbi_2(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    return ''.join(output)


print(ubbi_dubbi_2('octopus'))
print(ubbi_dubbi_2('elephant'))


# my new solution after seeing solution from book
def ubbi_dubbi_3(word: str) -> str:
    return ''.join([f'ub{letter}' if letter in 'aeiou' else letter for letter in word])

print(ubbi_dubbi_3('octopus'))
print(ubbi_dubbi_3('elephant'))
