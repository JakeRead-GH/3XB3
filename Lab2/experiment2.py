import graph
import bfsAndDfs
import random
import testingfunctions
import matplotlib.pyplot as plt

# 
def test_connections(num_nodes):
    connect_prob = []
    edges = []

    for num_edges in range(num_nodes-1, 100):
        print("Number of EDGES: " + str(num_edges))
        connect_found = 0
        # 10 Graphs for each number of edges
        for m in range(100):
            if graph.is_connected(testingfunctions.create_random_graph(num_nodes, num_edges)):
                connect_found += 1

        connect_prob.append(connect_found / 100)
        edges.append(num_edges)

    return edges, connect_prob


plt.title("Number of Edges vs. Connected Probability")
plt.xlabel("Number of Edges")
plt.ylabel("Connected Probability (%)")

edges, connect = test_connections(20)
plt.plot(edges, connect)
plt.show()