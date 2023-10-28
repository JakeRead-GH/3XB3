import lab3Helper


def ks_brute_force(items, capacity):
    powerset = lab3Helper.power_set(items)
    max_value = 0

    for subset in powerset:
        total_weight = sum(data[0] for data in subset)
        total_value = sum(data[1] for data in subset)
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value

    return max_value


def ks_rec_core(items, i, j):
    if not i or not j:
        return 0
    elif j - items[i - 1][0] < 0:
        return ks_rec_core(items, i - 1, j)
    else:
        return max(ks_rec_core(items, i - 1, j), ks_rec_core(items, i - 1, j - items[i - 1][0]) + items[i - 1][1])


def ks_rec(items, capacity):
    return ks_rec_core(items, len(items), capacity)


items = lab3Helper.generateRandomKnapsackItems(num_items=10)
#
# print(ks_brute_force(items, 10))
print(ks_rec(items, 20))

lab3Helper.plotTimingGraph("Bad Knapsack Testing", [ks_brute_force, ks_rec], 20, 20)
