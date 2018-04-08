# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this ias
# significantly more than half an hour of coding, so we’re doing it in pieces.
#
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
# not worrying about how the moves were made.
#
# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means
# that player 2 put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either
# in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every
# board there will only be one winner.


def check_winner(list1, list2, list3):
    for i in [1, 2]:
        if list1[0] == i and list1[1] == i and list1[2] == i:
            print('Player {} won'.format(i))
            quit()
        elif list2[0] == i and list2[1] == i and list2[2] == i:
            print('Player {} won'.format(i))
            quit()
        elif list3[0] == i and list3[1] == i and list3[2] == i:
            print('Player {} won'.format(i))
            quit()
        elif list1[0] == i and list2[1] == i and list3[2] == i:
            print('Player {} won'.format(i))
            quit()
        elif list1[2] == i and list2[1] == i and list3[0] == i:
            print('Player {} won'.format(i))
            quit()

    print('No winner')


test_list1 = [1, 1, 2]
test_list2 = [0, 2, 2]
test_list3 = [2, 0, 1]

check_winner(test_list1, test_list2, test_list3)
