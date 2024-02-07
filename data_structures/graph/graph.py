class Graph:

    @classmethod
    def construct_from(cls, file):
        with open(file, "r") as f:
            vertices = int(f.readline())
            _ = int(f.readline())

            graph = Graph(vertices)

            for line in f.readlines():
                v, w, = [int(i) for i in line.split()]
                graph.add_edge(v, w)

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = 0
        self.adjacents = []

        for i in range(self.vertices):
            self.adjacents.append([])

    def add_edge(self, v, w):
        self.adjacents[v].append(w)
        self.adjacents[w].append(v)
        self.edges += 1

    def degree(self, vertex):
        return len(self.adjacents[vertex])

    def max_degree(self):
        max_degree_ = 0
        for vertex in range(self.vertices):
            degree = self.degree(vertex)
            if degree > max_degree_:
                max_degree_ = degree

        return max_degree_

    def average_degree(self):
        return 2.0 * self.edges / self.vertices

    def num_of_self_loop(self):
        count = 0
        for vertex in range(self.vertices):
            for connection in self.adjacents[vertex]:
                if vertex == connection:
                    count += 1

        return count

    def to_string(self):
        s = f"{self.vertices} vertices, {self.edges} edges\n"
        for vertex in range(self.vertices):
            s += f"vertex-{vertex} : [" + ", ".join(self.adjacents[vertex]) + "]\n"

        return s
