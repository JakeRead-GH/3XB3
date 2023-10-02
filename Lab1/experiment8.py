import testingHelper
import bad_sorts
import good_sorts

testingHelper.plotTimingGraph("Experiment 8", [bad_sorts.insertion_sort, good_sorts.mergesort, good_sorts.quicksort], 25, 1, 1000, bad_sorts.create_random_list)