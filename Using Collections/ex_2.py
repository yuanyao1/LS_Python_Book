# Use slicing to write Python code to print a 6-character substring of 
# 'Launch School' that begins with the first c.

my_str = 'Launch School'
start_index = my_str.find('c')
end_index = start_index + 6
print(my_str[start_index:end_index])