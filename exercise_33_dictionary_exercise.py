# For this exercise, we will keep track of when our friend’s birthdays are, and
# be able to find that information based on their name. Create a dictionary (in your file)
# of names and birthdays. When you run your program it should ask the user to enter a name,
# and return the birthday of that person back to them. The interaction should look something like this:
#
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.


my_dictionary = {'Adam': '28 December', 'Monika': '20 July', 'Tom': '2 February'}


def my_func():
    print('Welcome to the birthday dictionary. We know the birthday of:')
    for key in my_dictionary:
        print(key)
    user_input = input('Who\'s birthday do you want to look up?')
    print('{}\'s birthday is on {}'.format(user_input, my_dictionary[user_input]))


if __name__ == '__main__':
    my_func()

# done
