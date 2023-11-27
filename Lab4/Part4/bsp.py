def bsp_val(L, m):
    dp = {}
    return bsp_val_core(dp, L, m)


def bsp_val_core(dp, L, m):
    if not L:
        return float("inf")
    elif not m:
        return min(L[i + 1] - L[i] for i in range(len(L) - 1))

    max_val = 0

    for i in range(len(L)):
        new_L = L.copy()
        del new_L[i]

        try:
            dp[tuple(new_L), m - 1]
        except KeyError:
            dp[tuple(new_L), m - 1] = bsp_val_core(dp, new_L, m - 1)

        val = dp[tuple(new_L), m - 1]

        if val > max_val:
            max_val = val

    return max_val


def bsp_solution(L, m):
    dp = {}
    val = bsp_val_core(dp, L, m)

    if val == float("inf"):
        return []

    for key in dp.keys():
        potential_solution = list(key[0])

        if min(potential_solution[i + 1] - potential_solution[i] for i in range(len(potential_solution) - 1)) == val:
            return potential_solution


L = [2, 4, 6, 7, 10, 14]
print(bsp_val(L, 2))
print(bsp_solution(L, 2))

L = [1]
print(bsp_solution(L, 2))
