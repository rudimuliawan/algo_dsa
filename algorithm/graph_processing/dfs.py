from data_structures.graph.graph import Graph


class DeepFirstSearch:

    def __init__(self, graph: Graph, s: int):
        self.marked = [False for _ in graph.vertices]
        self.count = 0
        self.dfs(graph, s)

    def dfs(self, graph: Graph, v: int):
        self.marked[v] = True
        self.count += 1

        for w in graph.adjacents[v]:
            if not self.marked[w]:
                self.dfs(graph, w)


class DeepFirstPaths:

    def __init__(self, graph: Graph, s: int):
        self.marked = [False for _ in graph.vertices]
        self.edge_to = [0 for _ in graph.vertices]
        self.s = s

    def dfs(self, graph: Graph, v: int):
        self.marked[v] = True
        for w in graph.adjacents[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(graph, w)

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
