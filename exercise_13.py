# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
# the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two
# numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci():
    user_input = int(input('How many numbers?'))

    number_1 = 0
    number_2 = 1
    number_3 = 1

    fibonacci_sequence = [number_1, number_2, number_3]

    while (user_input - 3) > 0:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        user_input -= 1

    return fibonacci_sequence

print(fibonacci())
