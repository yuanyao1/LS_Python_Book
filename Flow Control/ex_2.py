# assumption is argument passed to function is integer

# def even_or_odd(num):
#     if num % 2 == 0:
#         print('even')
#     else:
#         print('odd')

def even_or_odd(num):
    print('even' if num % 2 == 0 else 'odd')

def is_int(num):
    if type(num) == int:
        print(f'{num} is integer')
        even_or_odd(num)
    else:
        print(f'{num} is a {type(num)}')

# def even_or_odd(num):
#     match num:
#         case 0 if num % 2 == 0:
#             print('even')
#         case _:
#             print('odd')



is_int(5)
is_int('dog')
# print()

is_int(-3)
# even_or_odd(-3)
# even_or_odd(0)
# even_or_odd(6)
# even_or_odd(-12)