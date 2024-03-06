def solution(n, scores):
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = scores[0][0], scores[1][0]

    if n == 1:
        return max(dp[0][0], dp[1][0])

    dp[0][1] = scores[1][0] + scores[0][1]
    dp[1][1] = scores[0][0] + scores[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + scores[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + scores[1][i]

    return max(max(row) for row in dp)

T = int(input())
result = []

for _ in range(T):
    arr = []
    n = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().split(" "))))
    result.append(solution(n, arr))

[print(r) for r in result]