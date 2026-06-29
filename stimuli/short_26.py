"""
Complete the following code to insert into a Binary Search Tree (BST).

Example:
Suppose the BST currently contains: 10, 5, 15
* Shape of the tree before insertion:
*
*          10
*         /  \
*        5    15

Input:
key = 7

After insertion:
The BST contains: 10, 5, 7, 15
* Shape of the tree after insertion:
*
*          10
*         /  \
*        5    15
*         \
*          7
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None  # left and right subtrees
        self.right = None

def insert(root, key):
    """
    Inserts a node (key) into the binary search tree.
    
    Args:
        root: The root of the BST
        key: int key to insert
        
    Returns:
        The root of the BST 
    """
    new_node = Node(key)
    if root is None:  # tree is empty
        root = '''WRITE CODE HERE'''
        return root
    
    parent = None
    current = root
    
    while True:
        if current.key == key:
            return root  # key already exists, do nothing
        
        parent = '''WRITE CODE HERE'''
        
        if current.key < key:
            current = current.'''WRITE CODE HERE'''
            if current is None:
                parent.'''WRITE CODE HERE''' = '''WRITE CODE HERE'''
                return root
        else:
            current = current.'''WRITE CODE HERE'''
            if current is None:
                parent.'''WRITE CODE HERE''' = '''WRITE CODE HERE'''
                return root