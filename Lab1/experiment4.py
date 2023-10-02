import testingHelper
import good_sorts
import bad_sorts

testingHelper.plotTimingGraph("Good Sort Testing", [good_sorts.heapsort, good_sorts.mergesort, good_sorts.quicksort], 10000, 100, 5, bad_sorts.create_random_list)
