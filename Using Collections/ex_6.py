print('abc-def'.isalpha())      # False
print('abc_def'.isalpha())      # False
print('abc def'.isalpha())      # False
print('abc def'.isalpha() and   # False
      'abc def'.isspace())
print('abc def'.isalpha() or    # False
      'abc def'.isspace())
print('abcdef'.isalpha())       # True
print('31415'.isdigit())        # True
print('-31415'.isdigit())       # False
print('31_415'.isdigit())       # False
print('3.1415'.isdigit())       # False
print(' '.isspace())             # False