# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4
# to help you. Take this opportunity to practice using functions, described below.


def ex_1():
    user_input = int(input('Enter a number'))
    print(user_input)
    is_prime = True

    for i in range(2, user_input):
        if user_input % i == 0:
            is_prime = False

    if is_prime is True:
        print('{} IS prime'.format(user_input))
    elif is_prime is False:
        print('{} ISN\'T prime'.format(user_input))


ex_1()
