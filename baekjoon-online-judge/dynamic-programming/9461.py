def solution(n):
    if n <= 3:
        return 1
    elif n <= 5:
        return 2

    dp = [0] * (n+1)

    dp[1:4] = [1] * 3
    dp[4:6] = [2] * 2

    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[n]

N = int(input())
Pn = []

for _ in range(N):
    Pn.append(solution(int(input())))

[print(n) for n in Pn]