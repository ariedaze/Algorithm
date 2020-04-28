from singly_linked_list import SinglyLinkedList


class Queue(object):
    listInstance = SinglyLinkedList()

    def dequeue(self):
        return self.listInstance.removeAt(0)

    def enqueue(self, value):
        self.listInstance.insertAt(value, self.listInstance.getSize())



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.dequeue()
queue.dequeue()