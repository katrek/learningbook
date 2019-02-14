def main():
     # Create a bool variable to use as a flag.
    found = False

    search = input('Enter a description to search for: ')
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

     # Read the rest of the file.
    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')

        # Determine whether this record matches the search value.
        if descr == search:
             # Display the record.
             print('Description: ', descr)
             print('Quantity: ', qty)
             print()

             #Set the found flag to True.
             found = True
        descr = coffee_file.readline()
    coffee_file.close()

     # If the search value was not found in the file display a message.
    if not found:
         print('That item was not found in the file.')
main()