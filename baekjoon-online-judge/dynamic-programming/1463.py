def solution(x):
    if x == 1:
        return 0
    elif x <= 2:
        return 1

    dp = [0] * (x+1)
    dp[1], dp[2], dp[3] = 0, 1, 1

    for i in range(4, x+1):
        if i % 6 == 0:
            dp[i] = min(dp[i // 3], dp[i // 2], dp[i - 1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1

    #print(dp)
    return dp[x]

X = int(input())
print(solution(X))