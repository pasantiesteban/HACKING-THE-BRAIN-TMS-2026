"""
Below is a partial implementation of a singly linked list that maintains 
references to its head and tail nodes.

Complete the 'insert_before(key, item)' method so that it inserts 
a new element before the node containing the given key. 
If the list is empty, the method does nothing.

Example:
If the list contains: "A" -> "B" -> "C"
and insert_before("B", "X") is called,
the resulting list should be: "A" -> "X" -> "B" -> "C"
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.nxt = next_node

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_before(self, key, item):
        # if the list is empty, do nothing
        if """/* Write Code here */""" == None:
            return
        
        # if the head has the key
        if self.head.value == key:
            '''WRITE CODE HERE'''
            return
        
        # if the key is not in the head node
        prev = None
        cur = self.head
        while cur is not None and not '''WRITE CODE HERE''':  # while key not found
            prev = cur
            cur = cur.nxt
        
        # found the key, so we can perform the insertion
        if cur is not None:
           '''WRITE CODE HERE''' = Node(item, '''WRITE CODE HERE''')