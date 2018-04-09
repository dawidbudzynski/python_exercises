# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy
# numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers
# are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example,
# which I will describe below.)


file_one = open('primenumbers.txt', 'r')
file_one_content = file_one.read().split('\n')

file_two = open('happynumbers.txt', 'r')
file_two_content = file_two.read().split('\n')

common_elements = [number for number in file_one_content if number in file_two_content]

print(common_elements)

#done
