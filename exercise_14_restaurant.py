"""
In this exercise, I want you to create a new constant dict, called MENU, representing
the possible items you can order at a restaurant. The keys will be strings, and values
will be prices (i.e., integers). You should then write a function - restaurant - that asks
the user to enter an order:
    - if user enters the name of a dish on the menu, the program prints the price and running
      total. It then asks the user again for their order
    - if the user enter th name of adish not on the menu, the program scolds the user (mildly).
      it then asks the user again for their order.
    - if the user enters an empty string, the program stops prompting and prints total amount
"""
MENU = {'sandwitch': 30,
        'coffee': 20,
        'croissant': 25,
        'salad': 30}


# my solution
def restaurant():
    total = 0
    while True:
        order = input('Order: ')

        if order == '':
            print(f'Your total is {total}')
            break

        get_price = MENU.get(order)
        if get_price == None:
            print(f"Sorry, we don't have today {order} today, try something else")
        else:
            total += get_price
            print(f'{order} costs {get_price}, total is {total}')


# restaurant()

# solution from the book
MENU = {'sandwitch': 10, 'tea': 7, 'salad': 9}


def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip()

        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} costs {price}, total is {total}')
    print(f'Your total is {total}')


# Beyond the exercise
"""
create a dict in which the keys are usernames and the values are passwords 
both represented as strings. Create a tiny login system, in which the user must 
enter a username and password. If there is a match, then indicate that the user has 
successfully logged in. If not, the refuse them entry 
"""
USER_NAME = {'Tom': 'python_workout',
             'Putin': 'murderer'}


def log_sys():
    attempts = 0

    while attempts < 3:
        user = input('Enter your name: ')
        passwd = input('Password: ')
        val = validation(user, passwd)
        if val:
            print('Successful login!')
            break
        elif attempts == 2:
            print('You used all 3 attempts account blocked for 10 min')
            break
        else:
            attempts += 1
            print('Name or password incorrect try again: ')
            print(f'Remaining attempts {3 - attempts} out of 3')


def validation(name, password):
    # print(f'{USER_NAME.get(name, 0)} == {password}')
    return True if USER_NAME.get(name) == password else False


# log_sys()


"""
Define a dict whose keys are dates (represented by strings) from the most recent
week and whose values are temperatures. Ask the user to enter a date, and display
the temperature on that date, as well the previous and subsequent dates, if available 
"""

TEMP = {'1999-09-01': '26',
        '2022-04-22': '19',
        '2021-01-01': '5',
        '2022-04-23': '17',
        '2022-04-24': '13',
        '2022-04-25': '14',
        '2022-04-26': '14',
        '2023-01-01': '-1'
        }


def get_temp():
    year = input('Enter year in format (YYYY): ')
    month = input('Enter month in format (MM): ')
    day = input('Enter day in format (DD): ')
    user_date = '-'.join([x.strip(' .-+,;') for x in [year, month, day]])
    temperature = TEMP.get(user_date, False)
    before_text = f'Temperatures before {user_date}'
    after_text = f'Temperatures after {user_date}'
    before_temp, after_temp = temp_on_other_days(user_date)
    if temperature:
        print(f'\nTemperature on {user_date}: {temperature} Celsius')
        print_temperatures(sorted(before_temp), before_text)
        print_temperatures(sorted(after_temp), after_text)
    else:
        print(f'No data available for {user_date}')


def temp_on_other_days(user_date: str):
    before = [date for date in TEMP if (int(date[0:4]) < int(user_date[0:4])) or
              (int(date[0:4]) == int(user_date[0:4])) and
              (int(date[5:7]) <= int(user_date[5:7])) and
              (int(date[8:]) <= int(user_date[8:])) and
              (date != user_date)]

    after = [date for date in TEMP if (int(date[0:4]) > int(user_date[0:4])) or
             (int(date[0:4]) == int(user_date[0:4])) and
             (int(date[5:7]) >= int(user_date[5:7])) and
             (int(date[8:]) >= int(user_date[8:])) and
             (date != user_date)]

    return before, after


def print_temperatures(before_after: list, text: str):
    if before_after:
        print('-------------------------------')
        print(text)
        print('-------------------------------')
        for date in before_after:
            print(f'Temperature on {date}: {TEMP[date]} Celsius')

get_temp()
