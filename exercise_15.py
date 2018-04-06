# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say
# I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.


def exe_1():
    user_input = input('Enter long string')

    all_words_in_string = user_input.split(' ')

    all_words_reversed = all_words_in_string[::-1]

    return all_words_reversed


print(exe_1())
