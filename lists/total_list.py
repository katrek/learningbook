# This program calculates the total of the values
# in a list

def main():
    # Create a list

    a = int(input('Pick number 1: '))
    b = int(input('Pick number 2: '))
    c = int(input('Pick number 3: '))
    d = int(input('Pick number 4: '))

    numbers = [a, b, c, d]

    # Create a variable to use as an accumulator
    total = 0

    # Calculate the total of the list elements
    for value in numbers:
        total += value

    # Display the total of the list elements
    print('The total of the elements is', total)

main()