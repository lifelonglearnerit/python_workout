"""
Write a function, get_rainfall(), that tracks rainfall in a number of cities.
Users of your program will enter the name of a city; if the city name is blank,
then the function prints a report before exiting.
If the city name isn't blank then the program should also ask the user how much
rain has fallen in that city (typically measured in millimeters). After the user
enters the quantity of rain, the program again asks them for a city name, rainfall
amount and so on - until the user presses Enter instead of typing the name of a city.
When the user enters a blank city name, the program exits - but first, it reports how
much total rainfall there was in each city. Thus, if I enter:
Boston
5
New York
7
Boston
5
[Enter; blank line]
the program should output
Boston: 10
New York: 7
"""


# my solution
def get_rainfall():
    rainfall = dict()
    while True:
        print(rainfall)
        city = input('City: ')
        rain = input('Rainfall: ')
        if not city:
            for k, v in rainfall.items():
                print(f'{k}: {v}')
            break
        elif city not in rainfall.keys():
            rainfall[city] = int(rain)
        else:
            rainfall[city] += int(rain)


#get_rainfall()

# solution from the book
def get_rainfall():
    rainfall = {}
    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

# Beyond the exercise
"""
Instead of printing just the total rainfall for each city, print the total rainfall and
the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40 for 
Boston, you would see that total was 90 and the average was 30
"""

def get_rainfall_avg():
    rainfall = dict()
    while True:
        print(rainfall)
        city = input('City: ')
        rain = input('Rainfall: ')
        if not city:
            break
        elif city not in rainfall.keys():
            rainfall[city] = [int(rain)]
        else:
            rainfall[city].append(int(rain))

    for k, v in rainfall.items():
        print(f'City: {k}; Total Rainfall: {sum(v)}; Average Rainfall: {sum(v) / len(v)}')


#get_rainfall_avg()


def new_row(collection: list[str]) -> str:

    print(collection[0].rstrip('\n') + collection[1].strip(' ["\n') + collection[2].strip(' "\n'))



def cleaning_code(collection: list[str]) -> list[str]:
    new_log_file = list()
    item_index = 3
    for element in collection:
        element = element.rstrip('\n')

    for _ in range(int(len(collection) / 3)):
        new_row(collection[item_index-3:item_index])
        item_index += 3

def get_code():
    with open('exercise_15_log.txt', 'r') as log_file:
        log_file = log_file.readlines()
    cleaning_code(log_file)

get_code()


"""
helper exercise for log extraction: 
Write a function that takes list and returns list such as:
takes: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
returns: [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]]
"""
def list_of_lists(items: list[int]) -> list[list]:
    new_list = list()
    item_index = 3
    for _ in range(int(len(items))):
        new_list.append(items[item_index-3:item_index])
        item_index += 3
    return new_list
# print(list_of_lists([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))