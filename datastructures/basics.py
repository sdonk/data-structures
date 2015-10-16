class Stack(object):
    """
    Implements a stack type data structure
    """

    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        """
        Tests to see whether the stack is empty
        """
        return self.items == []

    @property
    def size(self):
        """
        Returns the number of items on the stack
        """
        return len(self.items)

    def push(self, item):
        """
        Adds a new item to the top of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack
        """
        try:
            return self.items.pop()
        except IndexError:
            raise Exception('The stack is empty')

    def peek(self):
        """
        Returns the top item from the stack but does not remove it
        """
        try:
            return self.items[-1]
        except IndexError:
            raise Exception('The stack is empty')


class Queue(object):
    """
    Implements a queue type data structure
    """

    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        """
        Tests to see whether the queue is empty
        """
        return self.items == []

    @property
    def size(self):
        """
        Returns the number of items on the stack
        """
        return len(self.items)

    def enqueue(self, item):
        """
        Adds a new item to the rear of the queue
        """
        self.items.index(0, item)

    def dequeue(self):
        """
        Removes and returns the front item from the queue
        """
        try:
            self.items.pop()
        except IndexError:
            raise Exception('The queue is empty')