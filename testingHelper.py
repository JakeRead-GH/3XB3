import bad_sorts
import good_sorts
import timeit
import matplotlib.pyplot as plt

def testSortingAlgorithm(algorithm, highest_list_length, step, runs_per_step, rand_list_generator):
    lengths = []
    times = []

    for i in range(0, highest_list_length, step):
        sub_times = []

        for j in range(runs_per_step):
            rand_list = rand_list_generator(i, i)

            start = timeit.default_timer()
            algorithm(rand_list)
            end = timeit.default_timer()

            sub_times.append(end - start)

            print(i)

        lengths.append(i)
        times.append(sum(sub_times) / runs_per_step)
    return lengths, times


def plotTimingGraph(graph_name, sorting_algorithms, highest_list_length, step, runs_per_step, rand_list_generator):
    plt.title(graph_name)
    plt.xlabel("List Length")
    plt.ylabel("Time (s)")

    algorithm_names = []

    for algorithm in sorting_algorithms:
        lengths, times = testSortingAlgorithm(algorithm, highest_list_length, step, runs_per_step, rand_list_generator)
        plt.plot(lengths, times)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.show()


#plotTimingGraph("Bad Sort Testing", [bad_sorts.bubble_sort, bad_sorts.insertion_sort, bad_sorts.selection_sort], 5000, 50, 1)
#plotTimingGraph("Good Sort Testing", [good_sorts.heapsort, good_sorts.mergesort, good_sorts.quicksort], 10000, 100, 5, bad_sorts.create_random_list)
