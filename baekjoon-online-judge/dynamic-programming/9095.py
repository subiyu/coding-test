def solution(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4

    dp = [0 for _ in range(n+1)]
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    return dp[n]

T = int(input())
results = []

for _ in range(T):
    n = int(input())
    results.append(solution(n))

[print(r) for r in results]