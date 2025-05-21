class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            "empty"
        pop_node = self.head
        self.head = self.head.next
        return pop_node

    def peek(self):
        if self.is_empty():
            "empty"
        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)

stack.pop()

print(stack.head)