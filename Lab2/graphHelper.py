import graph
import random


def has_edge(G, u, v):
    return u in G.adj and v in G.adj[u]


def random_graph(nodes, edges):
    if edges > nodes * (nodes - 1) // 2:
        edges = nodes * (nodes - 1) // 2
    G = graph.Graph(nodes)
    for _ in range(edges):
        u = random.randint(0, nodes - 1)
        v = random.randint(0, nodes - 1)
        while u == v or has_edge(G, u, v):
            u = random.randint(0, nodes - 1)
            v = random.randint(0, nodes - 1)
        G.add_edge(u, v)
    return G
