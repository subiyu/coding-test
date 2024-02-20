def solution(floor, ho):
    dp = [[0 for _ in range(ho+1)] for _ in range(floor+1)]
    dp[0] = [i for i in range(ho+1)]

    for i in range(1, floor+1):
        for j in range(1, ho+1):
            dp[i][j] = sum(dp[i-1][:j+1])
    return dp[floor][ho]


T = int(input())
results = []

for _ in range(T):
    k = int(input())
    n = int(input())
    results.append(solution(k, n))

[print(r) for r in results]

