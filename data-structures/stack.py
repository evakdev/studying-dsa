# Push, Pop, Peek, is_empty
from collections import deque

### With Deque
class Stack:
    def __init__(self):
        self.data = deque()
        self.size = 0

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return not bool(self.data)

    def peek(self):
        if not self.is_empty():
            return self.data[-1]


### with Array
class Stack:
    def __init__(self):
        self.data = list()
        self.size = 0

    def push(self, x):
        self.data.append(x)
        self.size += 1

    def pop(self):
        x = self.data.pop()
        self.size -= 1
        return x

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return not self.size


### with LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    def peek(self):
        return self.head

    def is_empty(self):
        return not self.size


a = Stack()
a.push(12)

a.push("a")
a.push("hi")
print(a)
print(a.peek())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.is_empty())
