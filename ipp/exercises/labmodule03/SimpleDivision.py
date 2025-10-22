def divideTwoNumbersWithExceptionHandling(a,b):
    '''Divides two numbers and handles division by zero.
    
    Key Arguments:
    a -- numerator (float or int)
    b -- denominator (float or int) '''
    try:
        answer =  a/b
        print(answer)
        return a/b
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
        return None
