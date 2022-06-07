import plotly.express as px


def main():
    equation_number = get_starting_values()
    equation = equations[equation_number - 1]
    # Iterate through the range of numbers from 1 to 100 as x
    # and generate the next value for y
    x_values = []
    y_values = []
    for x in range(0, 101):
        y = equation(x)
        # Append the x and y values to the lists
        x_values.append(x)
        y_values.append(y)
    plot(x_values, y_values)


# Calculate the next y values
def calculate_next_1(x):  # First equation
    return x ** 2


def calculate_next_2(x):  # Second equation
    return x ** 5


def calculate_next_3(x):  # Third equation
    return x ** 0.5


def calculate_next_4(x):  # Fourth equation
    return -x ** 5


equations = [calculate_next_1, calculate_next_2, calculate_next_3, calculate_next_4]


# Plot the calculated values
def plot(x, y):
    fig = px.line(x=x, y=y)
    fig.show()


def get_starting_values():
    print('There are 4 different equations to choose from.')
    print('Please enter the number (1 - 4) of the equation you would like to use:')
    equation_number = int(input())
    if equation_number < 1 or equation_number > 4:
        print('Please enter a number between 1 and 4.\n')
        equation_number = get_starting_values()

    return equation_number


if __name__ == '__main__':  # Only execute if this file is run directly and not imported
    main()
