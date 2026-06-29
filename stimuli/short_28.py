"""
Below is a partial implementation of a singly linked list that maintains 
references to its head and tail nodes.

Complete the 'add(index, item)' method so that it correctly inserts 
a new element at the specified index.

Example:
If the list contains: "A" -> "B" -> "C"
and add(1, "X") is called,
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
        self.size = 0
    
    def add(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = Node(item, self.head)
            self.size += 1
            if self.tail is None:
                self.tail = self.head
            return
        
        tmp = self.head
        for i in range(1,'''WRITE CODE HERE'''):
            tmp = tmp.nxt
        
        tmp.nxt = Node(item, '''WRITE CODE HERE''')
        
        if tmp.nxt.nxt is None:
            self.tail = '''WRITE CODE HERE'''

        self.size += 1