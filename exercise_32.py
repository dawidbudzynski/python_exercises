# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
# (head, body, 2 legs, and 2 arms) before they lose the game.
#
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the
#     letter and displaying that information to the user. In this exercise, we have to put it all together and add
#     logic for handling guesses.
#
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize
# them - let them guess again.
# Optional additions:
#
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is
#     challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!


from exercise_30_pick_random_word_from_file import pick_random_word


def menu():
    user_input = input('Do you want to play \'Hangman Game\'?\n').lower()
    if user_input == 'yes':
        winning_word = pick_random_word()
        guessing_phase(winning_word)
    elif user_input == 'no':
        print('Thanks for playing\n')
        quit()
    else:
        print('Unknown answer\n')
        menu()


def guessing_phase(correct_word):
    correct_word_list = list(correct_word.lower())
    correct_guesses = len(correct_word_list) * '_'
    correct_guesses_list = list(correct_guesses)
    used_letters = []
    number_of_guesses = 0
    while correct_word_list != correct_guesses_list:
        if number_of_guesses < 6:
            print('Chances left: {}\n'.format(6 - number_of_guesses))
            user_guess = input('Guess the letter: \n').lower()
            if user_guess in used_letters:
                print('You have used this letter before\n')
            else:
                if user_guess in correct_word_list:
                    indexes_of_letters = [index for index, ltr in enumerate(correct_word_list) if ltr == user_guess]
                    for index in indexes_of_letters:
                        correct_guesses_list[index] = user_guess
                    print(''.join(correct_guesses_list))
                else:
                    print('Incorrect letter\n')
                    number_of_guesses += 1
            used_letters.append(user_guess)
        else:
            print('You lost. You made 6 mistakes\n')
            menu()
    print('Congratulations!!! You won !!! You guesses: {} with {} mistakes.\n'.format(correct_word, number_of_guesses))
    menu()


if __name__ == '__main__':
    menu()
