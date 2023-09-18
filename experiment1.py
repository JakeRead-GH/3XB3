import bad_sorts
import timeit
import matplotlib.pyplot as plt


def testBubbleSort(highest_list_length, step):
    lengths = []
    times = []

    for i in range(0, highest_list_length, step):
        rand_list = bad_sorts.create_random_list(i, i)

        start = timeit.default_timer()
        bad_sorts.bubble_sort(rand_list)
        end = timeit.default_timer()

        lengths.append(i)
        times.append(end - start)

        print(i)
    return lengths, times


lengths, times = testBubbleSort(5000, 100)





