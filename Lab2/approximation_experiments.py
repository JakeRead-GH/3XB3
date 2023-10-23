import approximation as ap
import matplotlib.pyplot as plt
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

def testMVCAlgorithm(algorithm, graphs, lengths, per_step):
    sizes = []
    # for each edge length m, get the per_step average size of the MVC
    for m in range(len(lengths)):
        print(lengths[m])
        # Get average size of MVC for each graph per m
        size = 0
        for i in range(per_step):
            # get the size of the MVC for each graph offset by m
            size += len(algorithm(graphs[i+(m*per_step)]))
        sizes.append(size/per_step)
    print()
    return lengths, sizes
    

def experiment1():
    # Generate 1000 random graphs with 8 nodes and m edges
    # for m = 1, 5, 10, ..., 30
    # For each graph, compute the size of the minimum vertex cover
    per_step = 500
    graphs = []
    lengths = range(1, 75, 1)
    for m in lengths:
        for _ in range(per_step):
            G = random_graph(12, m)
            graphs.append(G)

    algorithms = [graph.MVC, ap.approx1, ap.approx2, ap.approx3]

    plt.title("Relationship between # of Edges and VC Size")
    plt.xlabel("# of Edges")
    plt.ylabel("VC Size")

    algorithm_names = []
    for algorithm in algorithms:
        lengths, sizes = testMVCAlgorithm(algorithm, graphs, lengths, per_step)

        plt.plot(lengths, sizes)
        if algorithm.__name__ != "MVC":
            algorithm_names.append(algorithm.__name__)
        else:
            algorithm_names.append("Actual")

    plt.legend(algorithm_names)
    plt.show()

print(experiment1())
