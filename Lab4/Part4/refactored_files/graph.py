class Graph:
    def __init__(self):
        self.adj = {}
        self.weights = {}

    def get_adj_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def get_number_of_nodes(self):
        return len(self.adj)


class WeightedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_weighted_edge(self, start, end, weight):
        super().add_edge(start, end, weight)

    def get_edge_weight(self, start, end):
        for edge in self.adjacency_list[start]:
            if edge[0] == end:
                return edge[1]
        return None


class HeuristicGraph(WeightedGraph):
    def __init__(self):
        super().__init__()
        self.heuristics = {}

    def add_heuristic(self, node, value):
        self.heuristics[node] = value

    def get_heuristic(self, node):
        return self.heuristics.get(node, 0)
