
class QueueIsEmptyException(Exception):
    pass


class Queue:
    class Node:

        def __init__(self, item, next_):
            self.item = item
            self.next = next_

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        old_last = self.last
        self.last = Queue.Node(item, None)

        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException()

        item = self.first.item
        self.first = self.first.next

        if self.is_empty():
            self.last = None

        return item

    def __iter__(self):
        self.current_position = self.first
        return self

    def __next__(self):
        if self.current_position is None:
            raise StopIteration()

        item = self.current_position.item
        self.current_position = self.current_position.next

        return item
