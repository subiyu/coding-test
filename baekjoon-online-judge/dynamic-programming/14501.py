def solution(n, times, prices):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        times[i-1] = times[i-1] + i

    for j in range(1, n+1):
        if times[j-1] > (n+1):
            dp[j] = 0
            continue
        arr = []
        for k in range(j-1, -1, -1):
            if times[k-1] <= j:
                arr.append(dp[k])
        if arr:
            dp[j] = max(arr) + prices[j-1]
        else:
            dp[j] = prices[j-1]

    return max(dp[1:])

N = int(input())
T = []
P = []

for _ in range(N):
    a, b = list(map(int, input().split(" ")))
    T.append(a)
    P.append(b)

print(solution(N, T, P))