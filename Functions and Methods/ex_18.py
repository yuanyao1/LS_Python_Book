def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
print(remainders_3(numbers_1))
print(any(remainders_3(numbers_1)))
print()
# [0, 1, 2, 0, 1, 2, 0]

numbers_2 = [1, 2, 4, 5]
print(remainders_3(numbers_2))
print(any(remainders_3(numbers_2)))
print()
# [1, 2, 1, 2]

numbers_3 = [0, 3, 6]
print(remainders_3(numbers_3))
print(any(remainders_3(numbers_3)))
print()
# [0, 0, 0]

numbers_4 = []
print(remainders_3(numbers_4))
print(any(remainders_3(numbers_4)))
# []