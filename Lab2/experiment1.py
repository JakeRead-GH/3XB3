import graph
import testingfunctions
import matplotlib.pyplot as plt


def test_cycles(num_nodes):
    cycle_prob = []
    edges = []

    for num_edges in range(3, 100):
        print("Number of EDGES: " + str(num_edges))
        cycles_found = 0
        # 10 Graphs for each number of edges
        for m in range(100):
            if graph.has_cycle(testingfunctions.create_random_graph(num_nodes, num_edges)):
                cycles_found += 1

        cycle_prob.append(cycles_found/100)
        edges.append(num_edges)

    return edges, cycle_prob


plt.title("Number of Edges vs. Cycle Probability")
plt.xlabel("Number of Edges")
plt.ylabel("Cycle Probability (%)")

edges, cycles = test_cycles(20)
plt.plot(edges, cycles)
plt.show()




