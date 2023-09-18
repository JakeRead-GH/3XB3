import bad_sorts
import timeit
import matplotlib.pyplot as plt


def testSortingAlgorithm(algorithm, highest_list_length, step):
    lengths = []
    times = []

    for i in range(0, highest_list_length, step):
        rand_list = bad_sorts.create_random_list(i, i)

        start = timeit.default_timer()
        algorithm(rand_list)
        end = timeit.default_timer()

        lengths.append(i)
        times.append(end - start)

        print(i)
    return lengths, times


def plotTimingGraph(sorting_algorithms, highest_list_length, step):
    plt.title("Bad Sort Testing")
    plt.xlabel("List Length")
    plt.ylabel("Time (s)")

    algorithm_names = []

    for algorithm in sorting_algorithms:
        lengths, times = testSortingAlgorithm(algorithm, highest_list_length, step)
        plt.plot(lengths, times)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.show()


plotTimingGraph([bad_sorts.bubble_sort, bad_sorts.insertion_sort, bad_sorts.selection_sort], 5000, 50)
