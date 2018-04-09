# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to
# play with some different code, use the code from the solution), and instead of printing the results
# to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.


from exercise_19_beautiful_soup_2 import all_p

file_title = input('How would you like to call this file?')
open_file = open('{}.txt'.format(file_title), 'w')
for paragraph in all_p:
    open_file.write(paragraph.text)
open_file.close()

# done
