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


#########
# Graph #
#########

class Vertex:
    """
    Implements a vertex type data structure
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph(object):
    """
    Implements a graph type data structure
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()
