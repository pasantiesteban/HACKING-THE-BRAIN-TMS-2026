"""
Complete a function to capitalize the first letter of each word in a
given string.

Example:
 Input:
 text = "hello world from python"

 Output after calling capitalize_first_letter(text):
 "Hello World From Python"
"""

def capitalize_first_letter(text):
    chars = list(text)

    for '''WRITE CODE HERE'''
        if x == 0 or chars[x - 1] == ' ':
            chars[x] = chars[x].upper()

    return "".join(chars)
