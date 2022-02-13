# write a function (run_timing) that asks how long it took you for you to run 10km
# The function continues to ask how long (in minutes) it took for additional runs
# until user presses Enter. At that point the function exits
# but only after calculating and displaying the average time that the 10 km runs took.

# mysolution
def run_timing():
    times = []
    while True:
        run_time = input('Enter 10km run time: ')
        if not run_time:
            print(f'Average 10km run time is {sum(times) / len(times):.2f}')
            break
        else:
            times.append(float(run_time))
run_timing()

# solution from the book
def run_timing():
    """Asks the urser repeatedly for numeric input. Prints the average time an
    d number of runs."""

    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break
        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')

run_timing()

# beyond the exercise
