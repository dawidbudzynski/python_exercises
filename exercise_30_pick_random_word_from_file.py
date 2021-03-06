# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
#
# In this exercise, the task is to write a function that picks a random word from a list of words from
# the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file
# is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each
# line in the file contains a single word.
#
# Hint: use the Python random library for picking a random word.


from random import choice


def pick_random_word():
    my_file = open('sowpods.txt', 'r')
    all_words = my_file.read().split('\n')
    my_file.close()
    random_word = choice(all_words)

    return random_word


if __name__ == '__main__':
    print(pick_random_word())

# done
