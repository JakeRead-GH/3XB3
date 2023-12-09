from shortestPathApprox import dijkstra_approx, bellman_ford_approx
import timeit
import matplotlib.pyplot as plt
from final_project_part1 import create_random_complete_graph


def varyingk_dijkstra_bellman():
    # Experiment 1
    graph = create_random_complete_graph(50, 5)


    plt.title("Varying K in Sparse vs. Dense Graphs")
    plt.xlabel("K values")
    plt.ylabel("Time (s)")









