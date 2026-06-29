"""
Complete a program to calculate x raised to the power y (x^y).

Sample Input:
 x = 7
 y = 2

Sample Output:
 49
"""

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x

    tmp = power('''WRITE CODE HERE''')
    tmp = tmp * tmp
    if y % 2 == 1:
        return x * tmp
    else:
        return tmp
