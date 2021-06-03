import unittest

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enque(self, item):
        self.stack1.push(item)

    def deque(self):
        if self.stack2.is_empty():
            while self.stack1.is_empty() is False:
                self.stack2.push(self.stack1.pop())


        return self.stack2.pop()


class test(unittest.TestCase):
    def test(self):
        myq = Queue()
        myq.enque(1)
        myq.enque(2)
        self.assertEqual(1, myq.deque())
        myq.enque(3)
        self.assertEqual(2, myq.deque())

unittest.main()
