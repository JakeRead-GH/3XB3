import bad_sorts
import good_sorts
import testingHelper
import math

# Ran into RecursionError explaining that the maximum depth was exceeded
# Resetting the recursion limit as 5000 instead of the standard 1000
import sys
sys.setrecursionlimit(5000)

testingHelper.plotTimingGraph("Good Near Sort Testing", [good_sorts.heapsort, good_sorts.mergesort, good_sorts.quicksort], int(1000*math.log(1000)//2), 50, 5, bad_sorts.create_near_sorted_list)
