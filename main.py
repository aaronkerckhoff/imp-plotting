def main():
    m, c = get_starting_values()
    # Iterate through the range of numbers from 1 to 100 as x
    # and generate the next value for y
    for x in range(1, 101):
        pass


def get_starting_values():
    m = int(input('Enter the number for m: '))
    c = int(input('Enter the number for c: '))
    return m, c


if __name__ == '__main__':
    main()
