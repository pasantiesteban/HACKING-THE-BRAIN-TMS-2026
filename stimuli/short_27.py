"""
Below is a partial implementation of a singly linked list.  
The list maintains references to its head and tail nodes, and no other fields.  

Complete the method '__len__()' so that it counts and returns 
the number of nodes currently stored in the list.

Example:
If the list contains: "A" -> "B" -> "C"
The method should return: 3
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.nxt = next_node

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __len__(self):
        count = 0
        tmp = self.head
        while '''WRITE CODE HERE''':
            '''WRITE CODE HERE'''
            count += 1
        return count
    