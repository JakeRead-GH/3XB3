from shortestPathApprox import dijkstra_approx, bellman_ford_approx
import timeit
import matplotlib.pyplot as plt
from final_project_part1 import DirectedWeightedGraph, total_dist, dijkstra_no_dest, bellman_ford, create_random_complete_graph
import random

# def create_random_graph(i, j, neg=False):
#     # Initializing graph with i nodes
#     rand_graph = DirectedWeightedGraph()

#     for i in range(i):
#         rand_graph.add_node(i)

#     # List and counter to keep track of existing edges
#     list_of_edges = []
#     edge_count = 0

#     while edge_count < j:
#         # Both nodes aren't equal
#         node1 = random.randint(0, i-1)
#         node2 = node1
#         while node1 == node2:
#             node2 = random.randint(0, i-1)

#         # Edge between unique nodes has not been formed yet
#         if [node1, node2] not in list_of_edges:
#             list_of_edges.append([node1, node2])
#             list_of_edges.append([node2, node1])
#             if neg:
#                 rand_graph.add_edge(node1, node2, random.randint(-100,100))
#             else:
#                 rand_graph.add_edge(node1, node2, random.randint(1,100))
#             edge_count += 1

#     return rand_graph

def create_sparse_graph(n, upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):  # Ensuring sparsity
            if random.random() > 0.5:  # Adjust this probability to control sparsity
                weight = random.randint(1, upper)
                G.add_edge(i, j, weight)
                G.add_edge(j, i, weight)
    return G

#EXPERIMENTS___________________________________________________________________

def experiment1_dijkstra():
    k_values = [i for i in range(1, 11)]

    dijkstra_r = []
    dijkstra_a = []

    for k in k_values:
        dijkstra_r_step = []
        dijkstra_a_step = []
        for _ in range(25):
            g = create_random_complete_graph(25, 1, 100)

            _, dist = dijkstra_no_dest(g, 0)
            dist.popitem()
            dijkstra_r_step.append(total_dist(dist))

            dist = dijkstra_approx(g, 0, k)
            dist.popitem()
            dijkstra_a_step.append(total_dist(dist))

        dijkstra_r.append(sum(dijkstra_r_step)/len(dijkstra_r_step))
        dijkstra_a.append(sum(dijkstra_a_step)/len(dijkstra_a_step))


    plt.title("Varying K Total Distance in Complete Graphs")
    plt.plot(k_values, dijkstra_r, label="Dijkstra")
    plt.plot(k_values, dijkstra_a, label="Dijkstra Approx")
    plt.xlabel("K Values")
    plt.ylabel("Total Distance")
    plt.xticks(k_values)
    plt.legend()
    plt.show()

def experiment1_bellman_ford():
    k_values = [i for i in range(1, 11)]

    bellman_r = []
    bellman_a = []

    for k in k_values:
        bellman_r_step = []
        bellman_a_step = []
        for _ in range(25):
            g = create_random_complete_graph(25, 1, 100)

            dist = bellman_ford(g, 0)
            dist.popitem()
            bellman_r_step.append(total_dist(dist))

            dist = bellman_ford_approx(g, 0, k)
            dist.popitem()
            bellman_a_step.append(total_dist(dist))

        bellman_r.append(sum(bellman_r_step)/len(bellman_r_step))
        bellman_a.append(sum(bellman_a_step)/len(bellman_a_step))
    
    plt.title("Varying K Total Distance in Complete Graphs")
    plt.plot(k_values, bellman_r, label="Bellman-Ford")
    plt.plot(k_values, bellman_a, label="Bellman-Ford Approx")
    plt.xlabel("K Values")
    plt.ylabel("Total Distance")
    plt.xticks(k_values)
    plt.legend()
    plt.show()

def experiment2_dijkstra(runs_per_k=500):
    k_values = [i for i in range(1, 9)]

    dijkstra_r = []
    dijkstra_a = []

    for k in k_values:
        dijkstra_r_step = []
        dijkstra_a_step = []
        for _ in range(runs_per_k):
            g = create_random_complete_graph(25, 1, 100)

            start = timeit.default_timer()
            dijkstra_no_dest(g, 0)
            end = timeit.default_timer()
            dijkstra_r_step.append((end - start)*1000)

            start = timeit.default_timer()
            dijkstra_approx(g, 0, k)
            end = timeit.default_timer()
            dijkstra_a_step.append((end - start)*1000)

        dijkstra_r.append(sum(dijkstra_r_step)/len(dijkstra_r_step))
        dijkstra_a.append(sum(dijkstra_a_step)/len(dijkstra_a_step))


    plt.title("Varying K Runtime in Complete Graphs")
    plt.plot(k_values, dijkstra_r, label="Dijkstra")
    plt.plot(k_values, dijkstra_a, label="Dijkstra Approx")
    plt.xlabel("K Values")
    plt.ylabel("Time (ms)")
    plt.xticks(k_values)
    plt.legend()
    plt.show()

def experiment2_bellman_ford(runs_per_k=500):
    k_values = [i for i in range(1, 9)]
    
    bellman_r = []
    bellman_a = []

    for k in k_values:
        bellman_r_step = []
        bellman_a_step = []
        for _ in range(runs_per_k):
            g = create_random_complete_graph(25, 1, 100)

            start = timeit.default_timer()
            bellman_ford(g, 0)
            end = timeit.default_timer()
            bellman_r_step.append((end - start)*1000)

            start = timeit.default_timer()
            bellman_ford_approx(g, 0, k)
            end = timeit.default_timer()
            bellman_a_step.append((end - start)*1000)

        bellman_r.append(sum(bellman_r_step)/len(bellman_r_step))
        bellman_a.append(sum(bellman_a_step)/len(bellman_a_step))

    plt.title("Varying K Runtime in Complete Graphs")
    plt.plot(k_values, bellman_r, label="Bellman-Ford")
    plt.plot(k_values, bellman_a, label="Bellman-Ford Approx")
    plt.xlabel("K Values")
    plt.ylabel("Time (ms)")
    plt.xticks(k_values)
    plt.legend()
    plt.show()

def experiment3(node_count, weight_upper):
    G = create_sparse_graph(node_count, weight_upper)
    avg_total_distances = []

    for source in range(node_count):
        _, dist = dijkstra_no_dest(G, source)
        total_distance = total_dist(dist)
        avg_distance = total_distance / (node_count - 1)
        avg_total_distances.append(avg_distance)

    plt.plot(range(node_count), avg_total_distances)
    plt.title('Average Total Distance from Each Source Node')
    plt.xlabel('Source Node')
    plt.ylabel('Average Total Distance')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    experiment1_dijkstra()
    experiment1_bellman_ford()
    experiment2_dijkstra(500)
    experiment2_bellman_ford(50)
    experiment3(300, 10)
