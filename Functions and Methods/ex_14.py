# Identify all of the identifiers on each line of the following code

def multiply(left, right):  # multiply (global), left(local), right(local)
    return left * right     # left(local), right(local)

def get_num(prompt):        # get_num(global), prompt(local)
    return float(input(prompt))     # prompt(local), float(built in), input(built in)

first_number = get_num('Enter the first number: ')      # first_number (global), get_num (global)
second_number = get_num('Enter the second number: ')    # second_number (global), get_num (global)
product = multiply(first_number, second_number)         # multiply (global), product(global), first_number(global), second_number(global)
print(f'{first_number} * {second_number} = {product}')  # print(built in), product(global), first_number(global), second_number(global)

# function names: multiply, get_num, input, float, print
# parameter names:
# left
# right
# prompt