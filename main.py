import plotly.express as px


def main():
    m, c = get_starting_values()
    # Iterate through the range of numbers from 1 to 20 as x
    # and generate the next value for y
    x_values = []
    y_values = []
    y = 1
    for x in range(1, 21):
        y = calculate_next_y(y, m, c)
        # Append the x and y values to the lists
        x_values.append(x)
        y_values.append(y)
    plot(x_values, y_values)


# Calculate the next y value based on the current y value
def calculate_next_y(y, m, c):
    return y * m + c


# Plot the calculated values
def plot(x, y):
    fig = px.line(x=x, y=y)
    fig.show()


def get_starting_values():
    m = float(input('Enter the number for m: '))
    c = float(input('Enter the number for c: '))
    return m, c  # Return the values as a tuple


if __name__ == '__main__':  # Only execute if this file is run directly and not imported
    main()
