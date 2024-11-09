def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remainders_5(numbers_1))
print(all(remainders_5(numbers_1)))
print()

numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
print(remainders_5(numbers_2))
print(all(remainders_5(numbers_2)))
print()

numbers_3 = [0, 5, 10]
print(remainders_5(numbers_3))
print(all(remainders_5(numbers_3)))
print()

numbers_4 = []
print(remainders_5(numbers_4))
print(all(remainders_5(numbers_4)))

# Use this function to determine which of the
# following lists do not contain any numbers that are divisible by 5: