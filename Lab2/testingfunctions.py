import graph
import random

def create_random_graph(i, j):
    # Initializing graph with i nodes
    rand_graph = graph.Graph(i)

    # List and counter to keep track of existing edges
    list_of_edges = []
    edge_count = 0

    while edge_count < j:
        # Both nodes aren't equal
        node1 = random.randint(0, i-1)
        node2 = node1
        while node1 == node2:
            node2 = random.randint(0, i-1)

        # Edge between unique nodes has not been formed yet
        if [node1, node2] not in list_of_edges:
            list_of_edges.append([node1, node2])
            list_of_edges.append([node2, node1])
            rand_graph.add_edge(node1, node2)
            edge_count += 1

    return rand_graph

