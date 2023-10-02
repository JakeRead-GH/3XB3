import bad_sorts
import good_sorts
import testingHelper

def bottom_up_mergesort(L):
    if len(L) == 0:
        return []

    window_container = []

    for i in range(0, len(L), 2):
        new_segment = L[i:i + 2]

        if len(new_segment) != 1 and new_segment[0] > new_segment[1]:
            new_segment[0], new_segment[1] = new_segment[1], new_segment[0]

        window_container += [new_segment]

    window_size = 2

    while window_size < len(L):
        new_window_container = []

        for i in range(0, len(window_container), 2):
            if i + 1 < len(window_container):
                new_window_container += [good_sorts.merge(window_container[i], window_container[i + 1])]
            else:
                new_window_container += [window_container[i]]

        window_container = new_window_container.copy()

        window_size *= 2

    return window_container[0]


#bottom_up_mergesort([9, 7, 3, 2, 0, 4, 6, 5, 5])

testingHelper.plotTimingGraph("Bottom Up Merge Testing", [good_sorts.mergesort, bottom_up_mergesort], 10000, 100, 10, bad_sorts.create_random_list)
