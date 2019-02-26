'''
The insert Method

The insert method allows you to insert an item into a
list at a specific position. You pass two arguments to
the insert method: an index specifying where the item
should be inserted and the item that you want to insert.
Program 7-5 shows an example.
'''

# This program demonstrates the insert method

def main():
    # Create a list with some names
    names = ['James', 'Kathryn', 'Bill']

    # Display the list
    print('The list before the insert:')
    print(names)

    # Insert a new name at element 0
    names.insert(0, 'Joe')

    # Display the list again
    print('The list after the insert:')
    print(names)
# Main function
main()