# Can you write some code to change the value 'bye' in the following tuple to
# 'goodbye'?


stuff = ('hello', 'world', 'bye', 'now')
stuff_list = list()

for element in stuff_list:
    if element != 'bye':
        stuff_list.append(element)
    else:
        stuff_list.append('Goodbye')

stuff = tuple(stuff_list)

print(stuff)
