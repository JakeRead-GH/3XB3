#************ Recursive Solution ************

def subset_sum_rec(numbers, target):
    if target == 0:
        return True
    if target < 0:
        return False
    if numbers == []:
        return False
    return subset_sum(numbers[:-1], target, d) or subset_sum(numbers[:-1], target - numbers[-1])


#************ Bottom Up Solution ************

def subset_sum_bottom_up(numbers, target):
    sp = [[False for j in range(target + 1)] for i in range(len(numbers) + 1)]
    for i in range(len(numbers) + 1):
        sp[i][0] = True
    for i in range(1, len(numbers) + 1):
        for j in range(1, target + 1):
            if numbers[i - 1] > j:
                sp[i][j] = sp[i - 1][j]
            else:
                sp[i][j] = sp[i - 1][j] or sp[i - 1][j - numbers[i - 1]]
    return sp[len(numbers)][target]


#************ Top Down Solution ************

def subset_sum_top_down(numbers, target):
    sp = {}
    for i in range(len(numbers) + 1):
        sp[(i,0)] = True
    for i in range(target + 1):
        sp[(0,i)] = i == 0
    top_down_aux(numbers, len(numbers), target, sp)
    return sp[(len(numbers),target)]


def top_down_aux(numbers, i, j, sp):
    if numbers[i - 1] > j:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        sp[(i, j)] = sp[(i - 1, j)]
    else:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        if not (i - 1, j - numbers[i - 1]) in sp:
            top_down_aux(numbers, i - 1, j - numbers[i - 1], sp)
        sp[(i, j)] = sp[(i - 1, j)] or sp[(i - 1, j - numbers[i - 1])]