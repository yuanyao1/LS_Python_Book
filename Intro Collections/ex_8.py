# print(list(range(3, 17, 4)))


# Are the lists assigned to my_list and another_list equal? yes
# Are the lists assigned to my_list and another_list the same object? no
# Are the nested lists at index 3 of my_list and another_list equal? yes
# Are the nested lists at index 3 of my_list and another_list the same object? yes

# my_list = [1, 2, 3, [4, 5, 6]]
# another_list = list(my_list)

# another_list[3][0] = 42

# print(my_list)
# print(another_list)

# print(id(my_list))
# print(id(another_list))

# a = 'dog barks'
# b = 'dog barks'
# print(id(a))
# print(id(b))
# print(id(a) == id(b))

# list_1 = [a, 10]
# list_2 = ['dog barks', 10]
# print(id(list_1[0]) == id(list_2[0]))
# print(list_1[0] is list_2[0])

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
print(names)