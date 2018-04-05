# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def ex_1():
    common = []

    for i in a:
        for j in b:
            if i == j:
                common.append(i)

    common = list(set(common))
    print(common)


def ex_2(a, b):
    first_list = []
    second_list = []
    common = []
    for i in range(a):
        first_list.append(randint(1, 10))
    for j in range(b):
        second_list.append(randint(1, 10))

    print(first_list)
    print(second_list)

    for i in first_list:
        for j in second_list:
            if i == j:
                common.append(i)

    common = list(set(common))

    print(common)


# ex_1()
ex_2(5, 10)
