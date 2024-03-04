def solution(n, numbers):
    dp = [0] * (n+1)
    if n == 1:
        return numbers[0]

    dp[1] = numbers[0]

    for i in range(2, n+1):
        dp[i] = max(dp[i-1]+numbers[i-1], numbers[i-1])

    return max(dp[1:])

N = int(input())
arr = list(map(int, input().split(" ")))
print(solution(N, arr))