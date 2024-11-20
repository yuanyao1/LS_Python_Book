numbers = [1, 2, 3, 4, 5]

# def modify_list(lst):
#     lst += [42]

# modify_list(numbers)
# print(numbers)


def modify_list(lst):
    lst.append(42)  # use an append method on the input argument
    #return lst      # specify a return value which can be used outside function

print(modify_list(numbers))


# def modify_list(lst):
#     lst.append(42)  # use an append method on the input argument
#     return lst      # specify a return value which can be used outside function

# print(modify_list(numbers))

# numbers = [1, 2, 3, 4, 5]

# def modify_list(lst):
#     lst = lst + [42]
#     return lst

# print(modify_list(numbers))
# print(numbers)