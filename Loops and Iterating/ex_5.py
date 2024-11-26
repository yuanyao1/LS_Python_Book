# Print all of the even numbers in the following list of nested lists. 
# Don't use any while loops

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for element in my_list:
    for sub_element in element:
        if sub_element % 2 == 0:
            print(sub_element)