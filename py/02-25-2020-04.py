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

2nd Strategy (without stack):
    1. ptr = None
    2. first_item.pointer = ptr
    3. first_item.pointer.pointer = first_item

Time complexity: O(n)
Space complexity: O(1)
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

    def reverse2(self):
        ptr = None
        item = self.head
        while item:
            next_item = item.pointer
            item.pointer = ptr
            ptr = item
            item = next_item
        self.head = ptr


linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))


print(linked_list)

linked_list.reverse2()

print(linked_list)

