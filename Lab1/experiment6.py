import good_sorts
import bad_sorts
import testingHelper

testingHelper.plotTimingGraph("Dual vs Single QuickSort Testing", [good_sorts.quicksort, good_sorts.dual_quicksort], 5000, 50, 5, bad_sorts.create_random_list)