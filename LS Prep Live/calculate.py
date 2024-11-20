# def calculate_area(length: int = 1, width: int = 1):
#     return length * width

# print(calculate_area())
# print(calculate_area(2, 4))

# Create a function called 'calculate_area' that takes the length and width of
# a rectangle as parameters and returns its area. Use default values of 1 for 
# both length and width.
# Create a few sample invocations to demonstrate its functionality.


# def calculate_area(length: int = 1, width: int = 1):
#     '''
#     This function takes in two integers representing the length and area of a 
#     rectangle and multiples them together to return the area.

#     Parameters:
#     length int
#     width int

#     Returns:
#     int: Area of the rectangle

#     Example:
#     >>> calculate_area()
#     1
#     >>> calculate_area(2, 4)
#     8

#     '''
#     return length * width

# print(calculate_area())
# print(calculate_area(2, 4))
# print(calculate_area(5))
# print(calculate_area(-15))


def calculate_area(length: float = 1, width: float = 1) -> str:
    '''
    This function takes in two floats representing the length and area of a 
    rectangle and multiples them together to return a string which contains the
    length, width, and area. An error will be raised if any arguments are not 
    greater than 0.

    Parameters:
    length (float): The length of the rectangle (default is 1)
    width (float): The width of the rectangle (default is 1)

    Returns:
    str: String that contains length, width, and calculated area.

    Example:
    >>> calculate_area()
    For a rectangle with length: 1 and width: 1, the area is 1
    >>> calculate_area(2, 4)
    For a rectangle with length: 2 and width: 4, the area is 8
    >>> calculate_area(2, -5)
    ValueError("The number given must be greater than 0.")

    '''
    if length <= 0 or width <= 0:
        raise ValueError(f'{'Length' if length <= 0 else 'Width'} given must '
                         f'greater than 0.'
                         )
    # if length <= 0:
    #     raise ValueError("Length given must be greater than 0.")
    # elif width <= 0:
    #     raise ValueError("Width given must be greater than 0.")
    
    rectangle_area = length * width
    
    return (
        f'For a rectangle with length: {length} and width: {width}, the area '
        f'is {round(rectangle_area, 2)}'
        )

print(calculate_area())
print(calculate_area(2, 4))
print(calculate_area(1.5, 4.5))
print(calculate_area(2.35, 5.689))
print(calculate_area(5, -4.7))


# def calculate_area(length: int = 1, width: int = 1):
#     if length <= 0 or width <= 0:
#         raise ValueError("The number given must be greater than 0.")
    
#     area = length * width
#     return f'For a rectangle with {length} and {width}, the area is {area}'

# print(calculate_area())
# print(calculate_area(2, 4))
# print(calculate_area(5))
# print(calculate_area(-15))