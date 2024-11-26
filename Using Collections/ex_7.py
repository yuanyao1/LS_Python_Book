# replace all the : characters in the string below with +


info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# info = info.replace(':', '+')
# print(info)


info_split = info.split(':')
print(info_split)
info = "+".join(info_split)
print(info)

# new_info = ""

# for char in info:
#     if char != ':':
#         new_info = new_info + char
#     else:
#         new_info = new_info + "+"

# info = new_info
# print(info)