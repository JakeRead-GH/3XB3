import good_sorts
import bad_sorts
import testingHelper

def dual_quicksort(L):
    if len(L) < 2:
        return L

    if L[0] < L[1]:
        first_pivot = L[0]
        second_pivot = L[1]
    else:
        first_pivot = L[1]
        second_pivot = L[0]

    left, right, middle = [], [], []

    for num in L[2:]:
        if num < first_pivot:
            left.append(num)
        elif first_pivot <= num <= second_pivot:
            middle.append(num)
        else:
            right.append(num)

    return dual_quicksort(left) + [first_pivot] + dual_quicksort(middle) + [second_pivot] + dual_quicksort(right)

testingHelper.plotTimingGraph("Dual vs Single QuickSort Testing", [good_sorts.quicksort, dual_quicksort], 5000, 50, 5, bad_sorts.create_random_list)