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


def ks_bottom_up(items, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(len(items) + 1):
        dp[i][0] = 0

    for j in range(capacity + 1):
        dp[0][j] = 0

    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if j - items[i - 1][0] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][0]] + items[i - 1][1])

    return dp[len(items)][capacity]


def ks_top_down_core(items, i, j, dp):
    if (i - 1, j) not in dp:
        ks_top_down_core(items, i - 1, j, dp)

    if j - items[i - 1][0] < 0:
        dp[(i, j)] = dp[(i - 1, j)]
    else:
        if (i - 1, j - items[i - 1][0]) not in dp:
            ks_top_down_core(items, i - 1, j - items[i - 1][0], dp)

        dp[(i, j)] = max(dp[(i - 1, j)], dp[(i - 1, j - items[i - 1][0])] + items[i - 1][1])


def ks_top_down(items, capacity):
    if not len(items) or not capacity:
        return 0

    dp = {}

    for i in range(len(items) + 1):
        dp[(i, 0)] = 0

    for j in range(capacity + 1):
        dp[(0, j)] = 0

    ks_top_down_core(items, len(items), capacity, dp)

    return dp[(len(items), capacity)]


def implementation2Experiments():
    lab3Helper.plotTimingGraph("Knapsack ks_rec and ks_brute_force runtime vs number of items", [ks_brute_force, ks_rec], 21, 50, 1, 5, 0, 10, 1, 10)
    lab3Helper.plotTimingGraph("ks_rec and ks_brute_force runtime vs number of items (Large v and w)", [ks_brute_force, ks_rec], 21, 500, 1, 5, 1000, 2000, 50, 75)


def tdbuExperiment():
    lab3Helper.plotTimingGraph("ks_bottom_up and ks_top_down runtime vs number of items (A)", [ks_bottom_up, ks_top_down], 100, 100, 1, 100, 0, 10, 1, 10)
    lab3Helper.plotTimingGraph("ks_bottom_up and ks_top_down runtime vs number of items (B)", [ks_bottom_up, ks_top_down], 100, 10000, 1, 2, 0, 1000, 1, 1000)
    lab3Helper.plotTimingGraph("ks_bottom_up and ks_top_down runtime vs number of items (C)", [ks_bottom_up, ks_top_down], 100, 10000, 1, 2, 1500, 1600, 1, 100)
    lab3Helper.plotTimingGraph("ks_bottom_up and ks_top_down runtime vs number of items (D)", [ks_bottom_up, ks_top_down], 100, 10000, 1, 2, 0, 1000, 1, 100)


if __name__ == "__main__":
    # Validation tests
    items = lab3Helper.generateRandomKnapsackItems(num_items=10)
    print(items)
    print(ks_rec(items, 10))
    print(ks_bottom_up(items, 10))
    print(ks_top_down(items, 10))

    # Implementation 2 Runtime Experiments
    implementation2Experiments()

    # Top Down vs Bottom Up Runtime Experiments
    tdbuExperiment()