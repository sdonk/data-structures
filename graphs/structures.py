# Represents a graph using adjacency list


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbour(self, neighbour, weight=0):
        self.connected_to[neighbour] = weight

    @property
    def connections(self):
        return self.connected_to.keys()

    def get_weight(self, neighbour):
        return self.connected_to[neighbour]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])


class Graph:
    def __init__(self):
        self._vertices = {}

    def __iter__(self):
        return self._vertices.items()

    @property
    def vertices(self):
        return self._vertices.keys()

    def add_vertex(self, key):
        self._vertices[key] = Vertex(key)
        return self._vertices[key]

    def get_vertex(self, key):
        return self._vertices.get(key)

    def add_edge(self, start, end, weight=0):
        if start not in self._vertices:
            self.add_vertex(start)
        if end not in self._vertices:
            self.add_vertex(end)
        self._vertices[start].add_neighbout(self._vertices[end], weight)
