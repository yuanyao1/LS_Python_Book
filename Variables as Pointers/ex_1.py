# my_object1 == my_object2
# my_object1 is my_object2

# first statement checks equality of the values assigned to each of the
# variables. If the values are equal then True is returned otherwise False

# second statement checks if the identity of the objects assigned to the
# variables is the same. If the variables have pointers to the same memory
# location that stores the object then True will be returned
my_lst = [1, 2]
my_tup = (1, 2)
my_lst2 = list(my_tup)

print(my_lst == my_tup)
print(my_lst is my_tup)

print(my_lst2[0] == my_tup[0])
print(my_lst2 is my_tup)
print(my_lst2)
print(my_tup)