class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # [4] -> [3] -> [2]
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            "empty"
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            "empty"
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node

    def peek(self):
        if self.is_empty():
            "empty"
        return self.head

    def is_empty(self):
        return self.head is None