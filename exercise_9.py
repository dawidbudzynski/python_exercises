# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then
# tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input
# lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


from random import randint


def game():
    winning_number = randint(1, 9)
    game_ended = False
    counter = 0

    while game_ended is False:
        user_guess = int(input('Enter a number'))
        if user_guess == 'exit':
            game_ended = True
        elif user_guess == winning_number:
            print('Congratulation, you won !!!, Guesses taken: {}'.format(counter))
            game_ended = True

        elif user_guess > winning_number:
            print('Try lower')
            counter += 1

        elif user_guess < winning_number:
            print('Try higher')
            counter += 1


game()
