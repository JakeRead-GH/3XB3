import sys

def num_of_wc_runs(n, m):
    dp = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = i - 1

    for j in range(1, m + 1):
        dp[1][j] = 0

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = min(max(dp[k][j - 1], dp[i - k][j]) for k in range(1, i)) + 1

    return dp[n][m]


def next_setting(n, m):
    if n == 1 or m == 1:
        return 1

    dp = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = i - 1

    for j in range(1, m + 1):
        dp[1][j] = 0

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = min(max(dp[k][j - 1], dp[i - k][j]) for k in range(1, i)) + 1

    lowest_steps = sys.maxsize
    for k in range(1, n):
        if max(dp[k][m - 1], dp[n - k][m]) < lowest_steps:
            lowest_steps = max(dp[k][m - 1], dp[n - k][m])
            best_k = k

    return best_k

print(num_of_wc_runs(100, 2))
print(next_setting(100, 2))