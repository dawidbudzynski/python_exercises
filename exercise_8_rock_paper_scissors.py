# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


def game():
    player_1 = input('Player 1 input: ')
    player_2 = input('Player 2 input: ')

    if player_1 == player_2:
        print('It\'s tie')
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            print('player 1 won')
        else:
            print('player 2 won')
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print('player 2 won')
        else:
            print('player 1 won')
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('player 1 won')
        else:
            print('player 2 won')


game()

# done
