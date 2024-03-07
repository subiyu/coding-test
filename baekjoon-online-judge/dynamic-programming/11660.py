import sys

N, M = list(map(int, sys.stdin.readline().split(" ")))
arr = []
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

for i in range(1, N + 1):
    dp[i][1] = dp[i - 1][1] + arr[i - 1][0]
    for j in range(2, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + arr[i - 1][j - 1] - dp[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split(" ")))
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])
