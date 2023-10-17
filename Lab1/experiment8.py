import testingHelper
import bad_sorts
import good_sorts

# ******************* Testing *******************
testingHelper.plotTimingGraph("Experiment 8", [bad_sorts.insertion_sort, good_sorts.mergesort, good_sorts.quicksort], 40, 1, 1000, bad_sorts.create_random_list)