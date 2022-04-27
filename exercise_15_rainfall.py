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


get_rainfall()

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

