# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import string
from random import (shuffle, choice)


def password_generator():
    user_lower = int(input('How many lower letters?'))
    user_upper = int(input('How many upper letters?'))
    user_numbers = int(input('How many numbers?'))
    user_punctuation = int(input('How many punctuation characters?'))

    punctuation = string.punctuation
    punctuation_list = [i for i in punctuation]
    shuffle(punctuation_list)

    lower_letters = string.ascii_lowercase
    lower_letters_list = [i for i in lower_letters]
    shuffle(lower_letters_list)

    upper_letters = string.ascii_uppercase
    upper_letters_list = [i for i in upper_letters]
    shuffle(upper_letters_list)

    numbers = string.digits
    numbers_list = [i for i in numbers]
    shuffle(numbers_list)

    result_list = []

    for i in range(user_lower):
        result_list.append(choice(lower_letters_list))
    for j in range(user_upper):
        result_list.append(choice(upper_letters_list))
    for k in range(user_numbers):
        result_list.append(choice(numbers_list))
    for l in range(user_punctuation):
        result_list.append(choice(punctuation_list))

    shuffle(result_list)

    result_string = ''
    for char in result_list:
        result_string += char

    return result_string


print(password_generator())
