import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': (3, 2, 'bb', 'bbb'),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
print()
# All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# # dict1['a'][0][0] = 100
# # print(dict1['a'])
# # print(dict2['a'])
# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])