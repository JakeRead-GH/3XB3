import random
import timeit
import matplotlib.pyplot as plt


def generateRandomKnapsackItems(num_items=10, min_v=0, max_v=10, min_w=1, max_w=10):
    knapsack = []
    for i in range(num_items):
        knapsack.append((random.randint(min_w, max_w), random.randint(min_v, max_v)))

    return knapsack


def power_set(s):
    if not s:
        return [[]]
    return power_set(s[1:]) + add_to_each(power_set(s[1:]), s[0])


def add_to_each(sets, element):
    copy = sets.copy()
    for s in copy:
        s.append(element)
    return copy


def testKnapsackAlgorithm(algorithm, max_num_items, capacity, step=1, runs_per_step=1, min_v=0, max_v=10, min_w=1, max_w=10):
    num_items = []
    times = []

    for i in range(0, max_num_items, step):
        sub_times = []

        for j in range(runs_per_step):
            items = generateRandomKnapsackItems(i, min_v, max_v, min_w, max_w)

            start = timeit.default_timer()
            algorithm(items, capacity)
            end = timeit.default_timer()

            sub_times.append(end - start)

            print(i)

        num_items.append(i)
        times.append(sum(sub_times) / runs_per_step)

    return num_items, times


def plotTimingGraph(graph_name, algorithms, max_num_items, capacity, step=1, runs_per_step=1, min_v=0, max_v=10, min_w=1, max_w=10):
    plt.title(graph_name)

    plt.xlabel("Number of Items")
    plt.ylabel("Time (s)")

    algorithm_names = []

    for algorithm in algorithms:
        num_items, times = testKnapsackAlgorithm(algorithm, max_num_items, capacity, step, runs_per_step, min_v, max_v, min_w, max_w)
        plt.plot(num_items, times)
        algorithm_names.append(algorithm.__name__)

    plt.legend(algorithm_names)
    plt.show()
