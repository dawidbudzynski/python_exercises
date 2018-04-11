# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your
# program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary
# defined in the program.
#
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file
# you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your
# JSON file should keep getting bigger and bigger.

import json
import os


def add_person_to_json():
    name = input('Enter a name')
    birthday_date = input('Enter a date')
    person_info = {name: birthday_date}
    if os.path.isfile('birthday_json_file.json') and os.access('birthday_json_file.json', os.R_OK):
        print("Record added to database")
        with open('birthday_json_file.json') as f:
            data = json.load(f)

        data.update(person_info)

        with open('birthday_json_file.json', 'w') as f:
            json.dump(data, f)

    else:
        print("Either file is missing or is not readable, creating birthday database...")
        with open('birthday_json_file.json', 'w') as my_file:
            json.dump(person_info, my_file)
            quit()


def read_from_json():
    with open('birthday_json_file.json', 'r') as my_file:
        all_people = json.load(my_file)
        print('People in database: ')
        for person in all_people:
            print(person)
        user_input = input('Who\'s birthday do you want to look up?')
        try:
            print('{}\'s birthday is on {}'.format(user_input, all_people[user_input]))
        except KeyError:
            print('No record in database')


def menu():
    user_choice = input('What to do? add/read')
    if user_choice == 'add':
        add_person_to_json()
    elif user_choice == 'read':
        read_from_json()
    else:
        print('Unknown choice')
        menu()


if __name__ == '__main__':
    menu()
