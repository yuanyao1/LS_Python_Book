dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
# print(dict1 is dict2)
# print(dict1['a'] is dict2['a'])
# print(dict1['b'] is dict2['b'])

dict2['a'][1] = 42
print(dict1['a'])   # [1, 42, 3]
print(dict1['a'] is dict2['a'])

print(dict1['b'] is dict2['b'])
dict2['b'] = 'dog'
print(dict1['b'])
print(dict1['b'] is dict2['b'])
print(dict2['b'])

# dict1['a'][1] = 42
# print(dict2['a'])   # [1, 42, 3]