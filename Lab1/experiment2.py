import testingHelper
import bad_sorts

# ******************* Insertion sort code *******************

def insertion_sort_variation(L):
    for i in range(1, len(L)):
        insert_variation(L, i)


def insert_variation(L, i):
    c = L[i]
    while i > 0:
        if c < L[i-1]:
            L[i] = L[i-1]
            i -= 1
        else:
            break
    L[i] = c

# ******************* Bubble sort code *******************

def bubble_sort_variation(L):
    for _ in range(len(L)):
        c = L[0]
        for j in range(len(L) - 1):
            if c > L[j+1]:
                L[j] = L[j+1]
            else:
                L[j] = c
                c = L[j+1]
        L[len(L)-1] = c


# ******************* Selection sort code *******************

# Selection sort but using min and max index
def selection_sort_variation(L):
    for i in range(len(L)//2):
        min_index, max_index = find_min_max_index(L, i)
        bad_sorts.swap(L, i, min_index)
        if i == max_index:
            max_index = min_index
        bad_sorts.swap(L, len(L)-1-i, max_index)

def find_min_max_index(L, n):
    min_index = n
    max_index = n
    for i in range(n+1, len(L)-n):
        if L[i] < L[min_index]:
            min_index = i
        if L[i] > L[max_index]:
            max_index = i
    return min_index, max_index

# Verify that the sorting algorithms work
# l1 = bad_sorts.create_random_list(1000, 110)
# l2 = l1.copy()
# bad_sorts.selection_sort(l1)
# bubble_sort_variation(l2)
# print(l1 == l2)

# ******************* Testing *******************
testingHelper.plotTimingGraph("Insertion Sort Testing", [bad_sorts.insertion_sort, insertion_sort_variation], 5000, 50, 2, bad_sorts.create_random_list)
testingHelper.plotTimingGraph("Bubble Sort Testing", [bad_sorts.bubble_sort, bubble_sort_variation], 2500, 50, 5, bad_sorts.create_random_list)
testingHelper.plotTimingGraph("Selection Sort Testing", [bad_sorts.selection_sort, selection_sort_variation], 5000, 100, 5, bad_sorts.create_random_list)