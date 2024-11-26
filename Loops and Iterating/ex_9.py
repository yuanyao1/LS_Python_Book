# Write a function that computes and returns the factorial of a number by 
# using a for or while loop. The factorial of a positive integer n, signified 
# by n!, is defined as the product of all integers between 1 and n, inclusive:


def factorial(number):
    result = 1

    while number > 0:
        result *= number
        number -= 1
    
    return result

# def factorial(number):
#     result = 1
#     for num in range(1, number + 1):
#         result *= num
    
#     return result

my_num = int(input("Give a positive integer: "))
print()
print(f'The factorial of {my_num} is {factorial(my_num)}')
