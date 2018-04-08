# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
# to largest) and another number. The function decides whether or not the given number is inside the list and
# returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.
import math

def check_list(my_list, check_number):
    new_list = my_list
    new_list_length = len(new_list)
    def check_middle(new_list):
        if new_list_length % 2 == 0:
            middle_element = my_list[new_list_length / 2]
            return middle_element
        else:
            middle_element = my_list[math.floor(new_list_length / 2)]
            return middle_element
    middle_element = check_middle(new_list)
    middle_element_index = new_list.index(middle_element)
    print('index:{}'.format(middle_element_index))
    print(middle_element)
    if middle_element == check_number:
        return True
    elif check_number > middle_element:
        new_list = my_list[middle_element_index:]
        print(new_list)
    elif check_number < middle_element:
        new_list = my_list[:middle_element_index]
        print(new_list)








a = [1, 3, 5, 30, 42, 43, 500]
my_number = 9

# todo finish