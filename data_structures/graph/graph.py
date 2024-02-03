class Graph:

    def __init__(self, num_of_vertices, num_of_edges):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.adjacents = []

        for i in range(self.num_of_vertices):
            self.adjacents.append([])

    def add_edge(self, v, w):
        self.adjacents[v].append(w)
        self.adjacents[w].append(v)

    def degree(self, vertex):
        return len(self.adjacents[vertex])

    def max_degree(self):
        max_degree_ = 0
        for vertex in range(self.num_of_vertices):
            degree = self.degree(vertex)
            if degree > max_degree_:
                max_degree_ = degree

        return max_degree_

    def average_degree(self):
        return 2.0 * self.num_of_edges / self.num_of_vertices

    def num_of_self_loop(self):
        count = 0
        for vertex in range(self.num_of_vertices):
            for connection in self.adjacents[vertex]:
                if vertex == connection:
                    count += 1

        return count

    def to_string(self):
        s = f"{self.num_of_vertices} vertices, {self.num_of_edges} edges\n"
        for vertex in range(self.num_of_vertices):
            s += f"vertex-{vertex} : [" + ", ".join(self.adjacents[vertex]) + "]\n"

        return s
