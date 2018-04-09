# Write a program (function!) that takes a list and returns a new list that contains all the elements
# of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def exe_1(my_list):
    new_list = list(set(my_list))
    return new_list


def exe_2(my_list):
    result = []

    for item in my_list:
        if item not in result:
            result.append(item)

    return result


example_list = [1, 1, 1, 3, 3, 4, 55, 55, 33]

# print(exe_1(example_list))

print(exe_2(example_list))

# done
