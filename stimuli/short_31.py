"""
Complete the following code to sort a list of integers using selection sort.

*Selection sort* repeatedly finds the smallest element from the unsorted portion 
of the list and swaps it with the first element of that portion. 
After each iteration, the sorted portion grows by one element.

Example:
Input:
[5, 2, 9, 1]

Output:
[1, 2, 5, 9]
"""

def selection_sort(data):
    for out_idx in range(0, '''WRITE CODE HERE'''):
        min_idx = out_idx  # set initial min value index
        
        # select a new min value index
        for in_idx in range('''WRITE CODE HERE''', '''WRITE CODE HERE'''):
            if data[in_idx] < data[min_idx]:  # if new min value
                min_idx = in_idx  # update min index
        
        # swap min value with first element of unsorted portion
        data['''WRITE CODE HERE'''], data[min_idx] = data[min_idx], data['''WRITE CODE HERE''']
        