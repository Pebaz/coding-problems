"""
Reverse a linked list

A linked list is just (data, pointer) where pointer is to the next element

Strategy:
    1. Create stack
    2. Push None
    3. Iterate through list, push each node to stack
    4. Assign end to head
    5. Pop off all items from stack, assign each new popped item to node pointer

Time complexity: O(n*2) meaning O(n)
Space complexity: O(n)
"""

class Node:
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        items = []
        item = self.head
        while item:
            items.append(item.data)
            item = item.pointer
        return str(items)

    def reverse(self):
        stack = [None]
        item = self.head

        while item:
            stack.append(item)
            item = item.pointer

        item = stack.pop()
        self.head = item

        while item:
            item.pointer = stack.pop()
            item = item.pointer

linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))


print(linked_list)

linked_list.reverse()

print(linked_list)

