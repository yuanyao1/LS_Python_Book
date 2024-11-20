# Write a function that takes a string as an argument and returns an all-caps 
# version of the string when the string is longer than 10 characters. 
# Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(string: str = 'Basketball') -> str:
    return string.upper() if len(string) > 10 else string

print(all_caps())
print(all_caps('dog'))
print(all_caps('charles barkeley'))
print(repr(all_caps('this is the beginning.')))