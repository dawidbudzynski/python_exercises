# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
#
# Extras:
#
# Add on to the previous program by asking the user for another number and printing out that many copies of
# the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as
# pressing the ENTER button)


def ex_1():
    name = input('Enter your name')
    age = input('Enter your age')
    number = input('Enter number')

    for i in range(int(number)):
        print('Hi, {}.You will turn 100 in {}'.format(name, 2018 + (100 - int(age))))


ex_1()

# done
