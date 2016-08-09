#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    user_input = ''
    while user_input == '':
        try:
            user_input = int(input('Enter an integer: '))
        except:
            print('Please enter an integer.')
    if user_input % 2 == 0:
        print("Even")
    else:
        print("Odd")

    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    pass


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    inc_n = 0
    for i in range(1,101):
        count = range(11,101,10)
        if inc_n < 9 and i == count[inc_n]:
            print('\n')
            inc_n += 1
        print('{:5}'.format(i), end = '')
    print('\n')
    pass


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = ''
    total = 0
    count = 0
    while True:
        try:
            user_input = input('Give a number to compute the average: ')
            if user_input == 'done':
                break
            else:
                total += float(user_input)
                count += 1
        except:
            print('Please enter a number.')
    return 'The average is ' + str(total/count)
    pass


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())
    pass

if __name__ == '__main__':
    main()
