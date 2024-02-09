from data_structures.graph.graph import Graph


class BreadthFirstPath:

    def __init__(self, graph: Graph, s: int):
        self.marked = [False for _ in graph.vertices]
        self.edge_to = [0 for _ in graph.vertices]
        self.s = s

        self.bfs(graph, s)

    def bfs(self, graph: Graph, s: int):
        self.marked[s] = True

        queue = [s]
        while queue:
            v = queue.pop(0)
            for w in graph.adjacents[v]:
                if not self.marked[v]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    queue.append(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return []

        path = []
        x = v
        while x != self.s:
            path.insert(0, x)
            x = self.edge_to[x]

        return path
