"""
Complete a program to multiply two integers without using multiplication,
division, bitwise operators, or loops.

Sample Input:
 x = 8, y = 9
Sample Output:
 72

Input:
 x = -11, y = 19
Output:
 -209
"""

def multiply_two_nums(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply_two_nums(x, y - 1)
    if y < 0:
        return  '''WRITE CODE HERE'''
