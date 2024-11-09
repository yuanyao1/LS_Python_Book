# Write a program that uses a multiply function to multiply two numbers and 
# returns the result. Ask the user to enter the two numbers, then output 
# the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

# first_number = float(input('Enter the first number: '))
# second_number = float(input('Enter the second number: '))

# def multiply(num1, num2):
#     return num1 * num2

# third_number = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {third_number}')


def multiply(num1, num2):
    return num1 * num2

def get_number(prompt):
    num = float(input(prompt))
    return num

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the first number: ')

print(f'{first_number} * {second_number} = {multiply(first_number, 
                                                     second_number)}')