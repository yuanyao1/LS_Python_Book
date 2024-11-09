# Write a function find_vowels that takes a string as an argument and returns a 
# list containing all of the vowels present in that string. The vowels should 
# only appear once in the output list and should be alphabetized.

# input from user
# function that parses each character in the input to check if vowel
# new list that stores each vowel
# sort vowel list in alphabetical order
# print out the vowel list

CHARACTERS = {'a', 'e', 'i', 'o', 'u'}

def find_vowels(string: str, characters: set) -> list:
    """
    This function takes in a string and a set and checks to see if the
    characters within the list are present in the string. It returns a unique
    list of the characters that are present and in alphabetical order.
    
    Parameters:
    string {str}: The string provided by the user.
    characters (set): A predetermined list of characters.

    Returns:
    list: A sorted list of the characters found within the string.

    Example:
    >>> find_vowels( 'I want that dog.', ('a', 'e', 'i', 'o', 'u'))
    ['a', 'i', 'o']
    >>> find_vowels( 'Origin species.', ('a', 'e', 'i', 'o', 'u'))
    ['e', 'i', 'o']
    """
    character_set = set()
    for char in characters:
        if char in string:
            character_set.add(char)
    return sorted(list(character_set))
   
def get_input() -> str:
    '''
    This function gets the user input and returns a string. It will continue to
    prompt user for input if none is given.
    '''

    my_input = ""
    while len(my_input) <= 0:
        my_input = input('Please input a string: ')
    return my_input.lower()

user_input = get_input()
vowels = find_vowels(user_input, CHARACTERS)
print(vowels)



     # vowel_set = {char for char in characters if char in string}
    # return sorted(vowel_set)

    #vowel_set = set()
    #print(type(vowel_set))
    # for vowel in characters:
    #     if vowel in string:
    #         vowel_set.add(vowel)
    # return sorted(list(vowel_set))

# def find_vowels(string):
#     vowel_list = []
#     for vowel in VOWELS:
#         if vowel in string:
#             vowel_list += vowel
#     return vowel_list


# Put thE Fork agAinst the wall nOw.
# ['a', 'e', 'i', 'o', 'u']

# Simple Plan
# ['a', 'e', 'i']