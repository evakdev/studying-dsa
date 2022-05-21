# Include creation, append, delete, insert, find, len, iter
# time yourself, add records and count of tries
# First Time complete series: 1 hour.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SinlglyLinkedList:
    def __init__(self, head=None, tail=None, ls=None):
        self.head = head
        self.tail = tail if tail else head
        self.size = 0
        if ls:
            self.construct(ls)

    def append(self, val):
        node = Node(val=val)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def insert(self, val, ind):
        """inserts val at index. index is zero-based."""
        if ind > self.size:
            raise IndexError

        node = Node(val=val)

        if ind == self.size:
            self.tail.next = node
            self.tail = node
        elif ind == 0:
            old_node = self.head
            self.head = node
            self.head.next = old_node
        else:
            current = self.head
            prev = self.head
            cnt = -1
            while current:
                cnt += 1
                if ind == cnt:
                    old_node = current
                    prev.next = node
                    node.next = old_node
                prev = current
                current = current.next
        self.size += 1

    def construct(self, ls):
        """Creates a linked list from values in an iterable"""
        for item in ls:
            self.append(item)

    def find(self, val):
        """Finds the first node with the value and returns an index for it
        index begins with zero."""
        ind = -1  # So that index is zero-based
        for i in self:
            ind += 1
            if i == val:
                return ind
        return None

    def delete(self, val):
        "Delete all nodes with the value."
        if not self.head:
            return

        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
        current = self.head
        prev = self.head

        while current:
            if current.val == val:
                prev.next = current.next
                current = current.next
                self.size -= 1
            else:
                prev = current
                current = current.next

    def __len__(self):
        return self.size

    def __iter__(self):

        current = self.head
        while current:
            yield current.val
            current = current.next

    def __str__(self):
        s = [str(i) for i in self]
        return f"SinglyLinkedList({', '.join(s)})"


a = SinlglyLinkedList(ls=[0, 1, 2, 4])

print(a)
a.insert(val=3, ind=4)
print(a)
