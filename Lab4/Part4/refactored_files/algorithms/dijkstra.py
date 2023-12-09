from ..graph import Graph
from ..min_heap import MinHeap, Element
from sp_algorithm import SPAlgorithm


class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int):
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        # Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node
            if current_node == dest:
                break

        return dist[dest]
