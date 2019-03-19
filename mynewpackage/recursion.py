def sum_array(array):
    summed = 0
    # check if item in array is a list (row) or just a value.
    for x in array:
        if isinstance(x, int):
            summed += x
        elif isinstance(x, list):
            summed += sum_array(x) # if x is a list recursively run the function.
        return summed
    '''Return sum of all items in array'''
  

def fibonacci(n):
  '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    '''Return nth term in fibonacci sequence'''
    
def factorial(n):
    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result
    '''Return n!'''

 

def reverse(word):
 '''Return word in reverse'''
    if len(word) == 0:
        return word
    else:
        return word[-1] + reverse(word[0:-1])
    '''Return word in reverse'''
