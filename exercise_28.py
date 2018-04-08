# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
#     All you need is some variables and if statements!


def find_max(number1, number2, number3):
    if number1 > number2:
        new_max = number1
    else:
        new_max = number2

    if number3 > new_max:
        new_max = number3
    print(new_max)


find_max(100, 2000, 27)
