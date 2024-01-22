def solution(elements):
    dp = [[0 for i in range(len(elements))] for j in range(len(elements))]
    sum_val = sum(elements)
    visited = [False] * (sum_val + 1)

    for i in range(len(elements)):
        dp[0][i] = elements[i]
        visited[dp[0][i]] = True

    for j in range(1, len(elements) - 1):
        for k in range(len(elements)):
            next = k + j
            if next >= len(elements):
                next -= len(elements)
            dp[j][k] = dp[j - 1][k] + elements[next]
            visited[dp[j][k]] = True

    return sum(visited) + 1