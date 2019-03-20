def sum_array(array):

    '''Return sum of all items in array'''

    # initialize variable.
    summed = 0

    # check if item in array is a list (row) or just a value.
    for x in array:
        if isinstance(x, int):
            summed += x
        elif isinstance(x, list):
            summed += sum_array(x) # if x is a list recursively run the function.
    return summed


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):

    '''Return n!'''

    if n == 0:
        return 1 # factorial of 0 is 1.
    else:
        return n*factorial(n-1)


def reverse(word):

    '''Return word in reverse'''

    if len(word) == 0:
        return word
    else:
        return word[-1] + reverse(word[0:-1])
