from ..graph import Graph
from ..min_heap import MinHeap, Element
from sp_algorithm import SPAlgorithm


class HeuristicPathFinder:
    def path_finder(self, graph, source, dest, heuristic):
        # g is a directed weighted graph from part1_function.py
        # s is the source node
        # d is the destination node

        pred = {}
        dist = {}
        q = MinHeap([])
        nodes = list(graph.adj.keys())

        for node in nodes:
            q.insert(Element(node, float("inf")))
            dist[node] = float("inf")

        q.decrease_key(source, 0 + [source])

        while not q.is_empty():
            current_element = q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key - heuristic[current_node]

            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node

                    q.decrease_key(neighbour, dist[neighbour] + heuristic[neighbour])
            if current_node == dest:
                break
        return dist[dest]


class A_Star(SPAlgorithm):
    def __init__(self, heurisitic_function):
        self.heuristic_function = heurisitic_function
        self.algorithm = HeuristicPathFinder()

    def sp_calc(self, graph: Graph, source, destination):
        return self.algorithm.path_finder(graph, source, destination, self.heuristic_function)
