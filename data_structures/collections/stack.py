class StackIsEmptyException(Exception):
    pass


class Stack:
    class Node:

        def __init__(self, item, below):
            self.item = item
            self.below = below

    def __init__(self):
        self.top = None

    def get_top(self):
        if self.top is None:
            raise StackIsEmptyException()

        return self.top.item

    def push(self, item):
        new_top = Stack.Node(item, self.top)
        self.top = new_top

    def pop(self):
        if self.top is None:
            raise StackIsEmptyException()

        item = self.top.item
        self.top = self.top.below
        return item

    def __iter__(self):
        self.current_position = self.top
        return self

    def __next__(self):
        if self.current_position is None:
            raise StopIteration()

        item = self.current_position.item
        self.current_position = self.current_position.below
        return item
