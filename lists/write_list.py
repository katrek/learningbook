# This program saves a list of string to a file

def main():
    cities = ['Kiev', 'Kharkov', 'Dnepr']

    # Open a file for writing
    outfile = open('cities.txt', 'w')

    # Write the list to the file
    for item in cities:
        outfile.write(item + '\n')

    # Close the file
    outfile.close()

main()