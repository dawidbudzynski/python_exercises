# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a
# string that reads the same forwards and backwards.)


def check_palindrome():
    user_input = input('Enter a word')

    input_backwards = user_input[::-1]

    if user_input == input_backwards:
        print('{} IS palindrome'.format(user_input))
    else:
        print('{} ISN\'T palindrome'.format(user_input))


check_palindrome()
