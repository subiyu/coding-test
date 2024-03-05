def solution(n):
    if n <= 2:
        return n

    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    return dp[n]

N = int(input())
print(solution(N))