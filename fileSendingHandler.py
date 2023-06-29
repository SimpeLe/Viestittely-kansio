import ascii
import string
import random


def createOneSourceCharacterList():
    """
    Creates 1Mb size file which inludes
    all alphabetic ascii characters in 
    arbitrary order 
    """
   
    # Create list of all characters
    #characters = string.printable
    characters = string.ascii_letters + string.digits + string.punctuation
    # add scandinavian characters
    characters +="äöå" 
    print(characters)
    # Randomize order of string
    #rand_string = ''.join(random.choice(characters) for _ in range(len(characters)))
    rand_string = ''.join(random.sample(characters, len(characters)))
    print(rand_string)
    return rand_string

    # Combine the required and remaining characters
    combined_string = uppercase_char + lowercase_char + digit_char + remaining_chars

    # Shuffle the characters to create the final random string
    random_string = ''.join(random.sample(combined_string, length))



createOneSourceCharacterList()
