import sys

num = int(sys.argv[1])

def fib(x):
    if x<2:
        return 1
    else:
        return fib(x-1) + fib(x-2) 
        
        
print fib(num)

def factorial(n):
    '''Returns the factorial of a positive integer
    
    F(N) = N * F(N-1)
    F(0) = 1
    
    >>> factorial(0)
    0
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(5)
    240
    
    '''
    assert n >= 0
    assert isinstance(n, int)
    return n*factorial(n-1)
