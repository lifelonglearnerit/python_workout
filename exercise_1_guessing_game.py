# write a function (guessing game) thate takes no arguments
# when run, the function chooses a random integer between 0 and 100
# then ask the user to guess what number has been chosen
# each time the user enters a guess, the program indicates one of the following: too high; too low; just right
# if the user guesses correctly the program exits otherwise user is asked to try again
# the program only exists after the user guesses correctly

import random

def guessing_game():
    chosen_number = random.randint(0, 100)
    while True:
        user_guess = int(input('Guess the number: '))
        if user_guess == chosen_number:
            print('Just right')
            exit('correct answer!')
        elif user_guess < chosen_number:
            print('Too low')
        else:
            print('Too high')
guessing_game()

"""
book answer:
def guessing_game().
    answer = random.randint(0, 100)
    
    while True:
        user_guess = int(input('What is your guess? '))
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer: 
            print(f'Your guess {user_guess}' is too low!)
        else:
            print(f'Your guess {user_guess}' is too high!)
            
guessing_game()
"""
