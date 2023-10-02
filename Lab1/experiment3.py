from bad_sorts import create_near_sorted_list
from bad_sorts import insertion_sort
from bad_sorts import selection_sort
from bad_sorts import bubble_sort
import math
from testingHelper import plotTimingGraph


plotTimingGraph("Bad Near Sort Testing", [bubble_sort, insertion_sort, selection_sort], int(1000*math.log(1000)//2), 100, 5, create_near_sorted_list)
