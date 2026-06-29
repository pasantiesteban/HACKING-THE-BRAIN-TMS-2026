"""
Complete the function 'isPalindrome' that checks if a given string is a palindrome.
A palindrome is a word that is spelled the same backwards such as "mom".
"""

def isPalindrome(s):
    left = 0
    right =  '''WRITE CODE HERE'''
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
