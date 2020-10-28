from singly_linked_list import SinglyLinkedList


class Stack(object):
    listInstance = SinglyLinkedList()

    def pop(self):
        return self.listInstance.removeAt(0)

    def push(self, value):
        self.listInstance.insertAt(value, 0)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()