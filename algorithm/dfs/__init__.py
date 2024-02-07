from data_structures.graph.graph import Graph


class DeepFirstSearch:

    def __init__(self, graph: Graph, s: int):
        self.marked = [False for _ in graph.vertices]
        self.count = 0
        self.dfs(graph, s)

    def dfs(self, graph: Graph, v: int):
        self.marked[v] = True
        self.count += 1

        for adj in graph.adjacents[v]:
            if not self.marked[adj]:
                self.dfs(graph, adj)
