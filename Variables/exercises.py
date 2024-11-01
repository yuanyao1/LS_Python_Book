# Classify the following potential function names as idiomatic,
# non-idiomatic, or illegal. For the non-idiomatic and illegal 
# names, explain your choice.

# Name          
# index         idiomatic
# CatName       non-idiomatic, no caps, need underscore
# lazy_dog      idiomatic
# quick_Fox     non-idiomatic, no caps
# 1stCharacter  illegal, no numbers first character
# operand2      idiomatic
# BIG_NUMBER    non-idiomatic, no caps
# π             non-idiomatic


# Classify the following potential constant names as idiomatic,
# non-idiomatic, or illegal. For the non-idiomatic and illegal
# names, explain your choice.

# Name          
# index         # non-idiomatic, needs uppercase
# CatName       # non-idiomatic, needs uppercase, needs underscore
# snake_case    # non-idiomatic, needs uppercase
# LAZY_DOG3     # idiomatic
# 1ST           # illegal, starts with number
# operand2      # non-idiomatic, needs uppercase
# BIG_NUMBER    # idiomatic
# Π             # non-idiomatic, stick with letters and numbers


# Questions 4
# Classify the following potential class names as idiomatic, non-idiomatic, 
# or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name          
# index         # non-idiomatic, first letter should be capitalized
# CatName       # idiomatic
# Lazy_Dog      # non-idiomatic, remove underscore
# 1ST           # illegal, starts with number
# operand2      # non-idiomatic, first letter should be capitalized
# BigNumber3    # idiomatic
# Πi            # non-idiomatic, non ASCII character


# Question 10
# obj = 'ABcd'          # reassigns to 'ABcd'
# obj.upper()           # neither
# obj = obj.lower()     # reassigns, converts to 'abcd'
# print(len(obj))       # neither, converts to int and then to string to print
# obj = list(obj)       # reassign, to list [a, b, c, d]
# obj.pop()             # mutate, 'd' is extracted and 'abc' remains
# obj[2] = 'X'          # mutate, ['a', 'b', 'X']
# obj.sort()            # mutate, ['X', 'a', 'b']
# set(obj)              # neither
# obj = tuple(obj)      # reassignment