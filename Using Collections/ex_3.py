# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple 
# should be in reverse order from the original. It should also exclude the 
# first and last members of the original. The result should be the 
# tuple (4, 3, 2)


my_tup = (1, 2, 3, 4, 5)
result = my_tup[-2:0:-1]
print(result)

# my_lst = list(my_tup)


# result = tuple(my_lst[3:0:-1])
# print(result)


# my_tup = (1, 2, 3, 4, 5)
# my_lst = list(my_tup)
# my_lst.pop()
# my_lst.pop(0)
# my_lst.reverse()
# result = tuple(my_lst)
# print(result)

# my_tup = my_tup[1:4]
# print(tuple(reversed(my_tup)))