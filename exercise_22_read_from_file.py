# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen. I have a .txt file for you, if you want to use it!
#
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
# and count how many of each “category” of each image there are. This text file is actually a list of files
# corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the
#     images. Once you take a look at the first line or two of the file, it will be clear which part represents
#     the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I
#     talked a little bit about it in this post.

from collections import Counter


def my_func():
    with open('nameslist.txt', 'r') as my_file:
        all_text = my_file.read()
        all_names = all_text.split('\n')
        all_names_counted = {}
        for name in all_names:
            all_names_counted[name] = all_names.count(name)
        print(all_names_counted)


def read_SUN_database():
    with open('SUN_file.txt', 'r') as my_file:
        all_text = my_file.read()
        all_lines = all_text.split('\n')
        all_categories = []
        for line in all_lines:
            if line[3:-25] != '':
                all_categories.append(line[3:-25])

        all_categories_counted = Counter(all_categories)

        for category, value in all_categories_counted.items():
            print('Category: {}, occurrences: {}'.format(category, value))


# my_func()
read_SUN_database()

# done
