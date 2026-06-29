"""
Complete the following code to merge two sorted lists into a new sorted list. 
Once the merge is done, return the merged list.

Example:
Input:
a = [1, 3, 5]
b = [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]
"""

def merge(a, b):
    # create a new list
    merged = [0] * (len(a) + len(b))  # create a new list of a given size (initially 0s)
    # initialize all of the indices
    index_a = 0
    index_b = 0
    index_m = 0
    
    # add correct values to the new list
    while index_a < '''WRITE CODE HERE''' and index_b < '''WRITE CODE HERE''':
        if a[index_a] < b[index_b]:
            merged[index_m] = a['''WRITE CODE HERE''']
            index_a += 1
        else:
            merged[index_m] = b['''WRITE CODE HERE''']
            index_b += 1
        index_m += 1
    
    # need to do some additional copying work here
    
   '''WRITE CODE HERE (may be multiple lines of code)''' 










    return merged