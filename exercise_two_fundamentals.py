'''
>>> JAAR
>>> 07/11/2023
>>> Practicing Fundamentals Program 2
>>> Version 1
'''

'''
>>> Asks the user for a range and then generate two random numbers within that range then swap both numbers if needed to ensure all of the following operations occur on the lowest of the two numbers:

1. Determine if they are odd
2. Calculate the sum of all numbers from the start of the range to the random number.
3. Print all even numbers from one random number to the other.
4. will then calculate the factorial for the lowest number.
'''

import random

def main() :
    # Assume there are two inputs separated by a ' '
    inputted_range = None
    inputted_range = input('Enter your range as two numbers separated by a space: ').split(' ')
    while not isinstance(inputted_range[0], int) and not isinstance(inputted_range[1], int) :
        try :
            inputted_range = [int(n) for n in inputted_range]
        except ValueError :
            inputted_range = input('\nYour input was invalid. Remember to enter two integers separated by a space: ').split(' ')

    print(f'\n Two numbers between {inputted_range[0]} and {inputted_range[1]} have been selected at random.\n')

    # Ensures the first entry is the lowest number.
    if inputted_range[0] > inputted_range[1] :
        inputted_range.reverse()

    random_ints = [random.randint(inputted_range[0], inputted_range[1]) for _ in range(2)]

    if random_ints[0] > random_ints[1] :
        random_ints.reverse()

    print(f'The two numbers are {random_ints[0]} and {random_ints[1]}.\n')

    # ERROR HAPPENING RIGHT HERE:
    check_if_odd = []
    for integer in random_ints :
        if integer % 2 == 1 :
            check_if_odd.append(True)
        else :
            check_if_odd.append(False)

    if check_if_odd[0] == True and check_if_odd[1] == True :
        print(f'\tBoth {random_ints[0]} and {random_ints[1]} are odd.')
    elif check_if_odd[0] == True :
        print(f'\tOnly {random_ints[0]} is odd.')
    elif check_if_odd[1] == True:
        print(f'\tOnly {random_ints[1]} is odd.')
    else :
        print('\tNeither number was odd.')

    factorial = None
    if random_ints[0] == 0 :
        factorial = 1
    elif random_ints[0] > 0:
        factorial = 1
        for n in range(random_ints[0], 0, -1) :
            factorial *= n
    else :
        factorial = 'Complex Number. Sorry'
    string_of_evens = None
    evens_list = [n for n in range(random_ints[0] + 1, random_ints[1]) if n % 2 == 0]
    if len(evens_list) != 0 :
        evens_list = (str(n) for n in evens_list)
        string_of_evens = ', '.join(evens_list)
    else :
        string_of_evens = 'None'

    print(f'''
        The calculations are as follows:
        
        \tSum for numbers from {inputted_range[0]} to {random_ints[0]}:\t\t{sum(range(inputted_range[0], random_ints[0] + 1))}
        \tFactorial of smallest int:\t\t{factorial}
        \tEvens Between both numbers:\t\t{string_of_evens}
        ''')

if __name__ == '__main__' :
    main()