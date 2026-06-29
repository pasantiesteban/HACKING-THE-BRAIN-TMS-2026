"""
Complete the definition of a function 'fibonacci'
so that it returns the nth Fibonacci number.
The sequence begins with 0 and 1, and each subsequent term is the sum of the two preceding terms.
You may write as many lines of code as you need to solve the problem.

Example:
Input:
n = 7

Output after calling fibonacci(n):
13
"""


def fibonacci(n):
    '''WRITE CODE HERE'''
    return fibonacci(n - 1) + fibonacci(n - 2)