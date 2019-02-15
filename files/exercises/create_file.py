def main():

    file_create = open('numbers.txt', 'w')

    num1 = (input('Enter 1st number: '))
    num2 = (input('Enter 2nd number: '))
    num3 = (input('Enter 3rd number: '))
    num4 = (input('Enter 4th number: '))
    num5 = (input('Enter 5th number: '))

    file_create.write(str(num1) + '\n')
    file_create.write(str(num2) + '\n')
    file_create.write(str(num3) + '\n')
    file_create.write(str(num4) + '\n')
    file_create.write(str(num5) + '\n')

main()

