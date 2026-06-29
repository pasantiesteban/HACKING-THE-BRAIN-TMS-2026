"""
 Complete the code below to search for a key in a Binary Search Tree (BST). 

 The method 'find' searches for a node with the given key and 
 returns true if the key is found, or false otherwise.

 Example:
 Suppose the BST contains the keys: 10, 5, 15, 3, 7

 Shape of the tree:
  
            10
            /  \
          5    15
         / \
        3   7
 
 
 Input:
 key = 7
 Output:
 true
 
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find(root, key):
    if root is None:  # tree is empty
        return False
    
    current = root  
    
    # while no match
    while current.key != key:
        if current.key < key:
            current = '''WRITE CODE HERE'''
        else:
            current = '''WRITE CODE HERE'''
        
        if current is '''WRITE CODE HERE''':  # not found
            return False
    
    return True  # found

