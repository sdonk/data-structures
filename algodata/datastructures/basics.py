class ParentStructure:
    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        return self.items == []

    @property
    def size(self):
        return len(self.items)


class Stack(ParentStructure):
    """
    Ordered LIFO

    https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
    """

    def push(self, item):
        """
        Adds a new item at the top of the stack
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


class Queue(ParentStructure):
    """
    Ordered FIFO

    https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

    Please note:
    Lists are not efficient for this purpose. While appends and pops from the end of list are fast,
    doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
    To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends
    """

    def enqueue(self, item):
        """
        Adds a new item to the back of the queue (right)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue (left)
        """
        try:
            return self.items.pop(0)
        except IndexError:
            raise Exception('The queue is empty')
