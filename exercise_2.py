# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
# message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def exercise_1():
    number_1 = int(input('Enter number'))

    if number_1 % 4 == 0:
        print('number can be divided by 4')
    elif number_1 % 2 == 0:
        print('number can be divided by 2')
    else:
        print("number can't be divided by 4 or 2")


def exercise_2():
    num = int(input('Enter number 1'))
    check = int(input('Enter number 2'))

    if num % check == 0:
        print('{} CAN be divided by {} evenly'.format(num, check))
    else:
        print('{} CAN\'T be divided by {} evenly'.format(num, check))


exercise_2()

# done
