import testingHelper
import bad_sorts

testingHelper.plotTimingGraph("Bad Sort Testing", [bad_sorts.bubble_sort, bad_sorts.insertion_sort, bad_sorts.selection_sort], 5000, 50, 1, bad_sorts.create_random_list)
