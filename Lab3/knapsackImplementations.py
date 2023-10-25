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


def ks_rec(items, capacity):
    a = 0


# print(ks_brute_force(lab3Helper.generateRandomKnapsackItems(num_items=10), 10))
# lab3Helper.plotTimingGraph("Knapsack Brute Force Test", [ks_brute_force], 20, 20)
