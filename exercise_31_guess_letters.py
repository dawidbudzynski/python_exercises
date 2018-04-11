# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
# guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual
# game, the player can only guess 6 letters incorrectly before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
# guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
# infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and
# display a different message if the player tries to guess that letter again. Remember to stop the game when all the
# letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of
# guesses the player has remaining - we will deal with those in a future exercise.
#
# An example interaction can look like this:
#
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.


correct_word = 'EVAPORATE'
correct_word_list = list(correct_word)
correct_guesses = '_________'
correct_guesses_list = list(correct_guesses)
used_letters = []

print('Welcome to Hangman!')

while correct_word_list != correct_guesses_list:
    user_guess = input('Guess the letter: ').upper()
    if user_guess in used_letters:
        print('You have used this letter before')
    else:
        if user_guess in correct_word_list:
            indexes_of_letters = [index for index, ltr in enumerate(correct_word_list) if ltr == user_guess]
            for index in indexes_of_letters:
                correct_guesses_list[index] = user_guess
            print(''.join(correct_guesses_list))
        else:
            print('Incorrect letter')
    used_letters.append(user_guess)
print('Congratulations!!! You won !!!')

# done
