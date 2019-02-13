def main():
    # Controlling the loop
    another = 'y'

    # Opening the coffee.txt in append mode
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file
    while another == 'y' or another == 'Y':
        # Get the coffee record data
        print('Enter the following coffee data: ')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        # Append data to the file
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Choose to add more
        print('You want to add more info?')
        another = input('Y = Yes, anything else = no')

    # Close the file
    coffee_file.close()
    print('Data saved to coffee.txt')

main()
