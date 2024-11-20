people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

print(people_phones.keys())
# dict_keys(['Chris', 'Pete', 'Clare'])

print(people_phones.values())
# Pretty printed for clarity
# dict_values([
#     '111-2222',
#     '333-4444',
#     '555-6666'
# ])

print(people_phones.items())
# Pretty printed for clarity
# dict_items([
#     ('Chris', '111-2222'),
#     ('Pete',  '333-4444'),
#     ('Clare', '555-6666')
# ])

# my_set = {5, 3.14, -2.71}
# print(min(my_set), max(my_set))      # -2.71 3.14

# my_dict = {
#     'a': 'abc',
#     37: 'def',
#     (5, 6, 7): 'ghi',
#     frozenset([1, 2]): 'jkl',
# }

# my_dict['a'] = 'ABC'
# my_dict[37] = 'DEF'
# my_dict[(5, 6, 7)] = 'GHI'
# my_dict[frozenset([1, 2])] = 'JKL'
# print(my_dict)


# my_dict['xyz'] = 'Investment'
# print(my_dict)

# my_dict[[1, 2, 3]] = 'Hey there!'
# TypeError: unhashable type: 'list'

# Pretty printed for clarity
# {
#     'a': 'ABC',
#     37: 'DEF',
#     (5, 6, 7): 'GHI',
#     frozenset({1, 2}): 'JKL'
# }