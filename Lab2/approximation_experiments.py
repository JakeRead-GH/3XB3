import approximation as ap
import matplotlib.pyplot as plt
import graph
import statistics
import numpy as np

#==========================Helper Functions=======================
import graphHelper


def testMVCAlgorithm(algorithm, graphs, lengths, per_step):
    sizes = []
    # for each edge length m, get the per_step average size of the MVC
    for m in range(len(lengths)):
        print(lengths[m])
        # Get average size of MVC for each graph per m
        res = []
        for i in range(per_step):
            # get the size of the MVC for each graph offset by m
            res.append(len(algorithm(graphs[i+(m*per_step)])))
        sizes.append(statistics.mean(res))
    print()
    return lengths, sizes


#===========================Experiments===========================

def experiment1():
    per_step = 100
    num_of_nodes = 12
    graphs = []
    lengths = range(1, 75)
    for m in lengths:
        for _ in range(per_step):
            G = graphHelper.random_graph(num_of_nodes, m)
            graphs.append(G)

    algorithms = [graph.MVC, ap.approx1, ap.approx2, ap.approx3]

    plt.title("Relationship between # of Edges and VC Size (Mean)")
    plt.xlabel("# of Edges")
    plt.ylabel("VC Size")

    algorithm_names = []
    for algorithm in algorithms:
        lengths, sizes = testMVCAlgorithm(algorithm, graphs, lengths, per_step)

        plt.plot(lengths, sizes)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.show()

def experiment2():
    per_step = 100
    num_of_edges = 5
    graphs = []
    lengths = range(4, 18)
    for n in lengths:
        for _ in range(per_step):
            G = graphHelper.random_graph(n, num_of_edges)
            graphs.append(G)

    algorithms = [graph.MVC, ap.approx1, ap.approx2, ap.approx3]

    plt.title("Relationship between # of Nodes and VC Size (Mean)")
    plt.xlabel("# of Nodes")
    plt.ylabel("VC Size")

    algorithm_names = []
    for algorithm in algorithms:
        lengths, sizes = testMVCAlgorithm(algorithm, graphs, lengths, per_step)

        plt.plot(lengths, sizes)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.xticks(np.arange(4, 18, 1))
    plt.yticks(np.arange(2, 12, 1))
    plt.show()

def experiment2_modified():
    per_step = 100
    num_of_edges = 15
    graphs = []
    lengths = range(4, 100)
    for n in lengths:
        for _ in range(per_step):
            G = graphHelper.random_graph(n, num_of_edges)
            graphs.append(G)

    algorithms = [ap.approx1, ap.approx2, ap.approx3]

    plt.title("# of Nodes vs VC Size (No MVC)")
    plt.xlabel("# of Nodes")
    plt.ylabel("VC Size")

    algorithm_names = []
    for algorithm in algorithms:
        lengths, sizes = testMVCAlgorithm(algorithm, graphs, lengths, per_step)

        plt.plot(lengths, sizes)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.show()


if __name__ == "__main__":
    experiment1()
    experiment2()
    experiment2_modified()
