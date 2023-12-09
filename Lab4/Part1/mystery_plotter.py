from final_project_part1 import create_random_complete_graph, mystery
import time
import matplotlib.pyplot as plt
import numpy as np

def mystery_experiments(min_nodes, max_nodes, step):
    times = []
    sizes = []
    for i in range(min_nodes, max_nodes, step):
        G = create_random_complete_graph(i, 10)  # Generate a random graph
        start_time = time.time()
        mystery(G)
        end_time = time.time()
        times.append(end_time - start_time)
        sizes.append(i)


    print("Sizes: ", sizes)
    print("Times: ", times)
    plt.loglog(sizes, times)
    plt.xlabel('Number of Nodes (log scale)')
    plt.ylabel('Execution Time (log scale)')
    plt.title('Log-Log Plot of Execution Time vs Graph Size')
    plt.show()

mystery_experiments(10, 500, 10)