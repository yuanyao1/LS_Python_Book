import copy

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
# set1.add(range(5, 10))
# print(set2)
# print(set1 is set2)
# {42, 'Monty Python', ('a', 'b', 'c')}

print(set1 is set2)
print(id(set1))
print(id(set2))
set1.remove('Monty Python')
print(f'{set2} has id {id(set2)}')
print(f'{set1} has id {id(set1)}')