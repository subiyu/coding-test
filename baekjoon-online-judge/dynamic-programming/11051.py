def solution(n, k):
    #nCk, nC1 = n, nC0 = 1, nCn=1
    dp = [[0 for _ in range(i+1)] for i in range(n+1)]

    for m in range(1, n+1):
        dp[m][0], dp[m][m] = 1, 1

    for i in range(1, n+1):
        for j in range(1, i):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

    return dp[n][k]

N, K = map(int, input().split(" "))
print(solution(N, K))