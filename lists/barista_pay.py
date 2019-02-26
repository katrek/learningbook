'''
Megan owns a small neighborhood coffee shop, and she has six employees
 work as baristas (coffee bartenders). All of the employees have the
 same hourly pay rate. Megan has asked you to design a program that will
 allow her to enter the number of hours worked by each employee, then display
 the amounts of all the employees’ gross pay. You determine the program should
 perform the following steps:

1. For each employee: get the number of hours worked and store it in a list element.

2. For each list element: use the value stored in the element to calculate
an employee’s gross pay. Display the amount of the gross pay.


'''

# This program calculates the gross pay for
# each of Megan's baristas

# NUM_EMPLOYEES is used as a constant for the
# size of the list

NUM_EMPLOYEES = 6

def main():
    # Create a list to hold employee hours
    hours =[0] * NUM_EMPLOYEES

    # Get each employee's hours worked
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by emplyee ',
              index + 1, ': ', sep='', end='')
        hours[index] = float(input())

    # Get the hourly pay rate
    pay_rate = float(input('Enter the hourly pay rate: '))

    # Display each employee's gross pay
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ', index +1, ': $',
              format(gross_pay, ',.2f'), sep='')
main()