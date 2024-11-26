# Part 1: Write some code to print Bark by accessing the element associated 
# with the key Dog.

# Part 2: Write some code to print None when you try to print the value 
# associated with the non-existent key, Lizard.

# Part 3: Write some code to print <silence> when you try to print the 
# value associated with the non-existent key, Lizard.

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])

print(pets.get('Lizard'))

print(pets.get('Lizard', '<silence>'))

# Which of the following values can't be used as a key in a dict object, 
# and why?

# 'cat'                         # yes
# (3, 1, 4, 1, 5, 9, 2)         # yes
# ['a', 'b']                    # no, mutable
# {'a': 1, 'b': 2}              # no, mutable
# range(5)                      # yes
# {1, 4, 9, 16, 25}             # no, mutable
# 3                             # yes
# 0.0                           # yes
# frozenset({1, 4, 9, 16, 25})  # yes