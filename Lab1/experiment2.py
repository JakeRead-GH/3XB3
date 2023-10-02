def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

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
    # n=0
    for i in range(len(L)):
        c = L[0]
        for j in range(len(L) - 1):
            if c > L[j+1]:
                L[j] = L[j+1]
                if j+1>= len(L)-1:
                    L[j+1]= c
                # n+=1
            elif c < L[j+1]:
                L[j] = c
                c = L[j+1]
                # n+=1
            # print(L)
        # print()


# ******************* Selection sort code *******************

# Selection sort but using min and max index
def selection_sort_variation(L):
    for i in range(len(L)//2):
        min_index, max_index = find_min_max_index(L, i)
        swap(L, i, min_index)
        if i == max_index:
            max_index = min_index
        swap(L, len(L)-1-i, max_index)

def find_min_max_index(L, n):
    min_index = n
    max_index = n
    for i in range(n+1, len(L)-n):
        if L[i] < L[min_index]:
            min_index = i
        if L[i] > L[max_index]:
            max_index = i
    return min_index, max_index

# l1 = bad_sorts.create_random_list(10000, 100)
# l2 = l1.copy()

# bad_sorts.selection_sort(l1)
# experiment2.selection_sort_variation(l2)

# print(l1 == l2)
# plotTimingGraph("Insertion Sort Testing", [bad_sorts.insertion_sort, experiment2.insertion_sort_variation], 5000, 50, 1, bad_sorts.create_random_list)
# plotTimingGraph("Bubble Sort Testing", [bad_sorts.bubble_sort, experiment2.bubble_sort_variation], 5000, 50, 1, bad_sorts.create_random_list)
# plotTimingGraph("Selection Sort Testing", [bad_sorts.selection_sort, experiment2.selection_sort_variation], 5000, 100, 5, bad_sorts.create_random_list)

