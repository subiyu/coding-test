def solution(n, numbers):
    if n == 1:
        return numbers[0]
    elif n == 2:
        return numbers[0] + numbers[1]

    dp = [0] * (n+1)
    dp[1] = numbers[0]
    dp[2] = numbers[0] + numbers[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+numbers[i-2]+numbers[i-1], dp[i-2]+numbers[i-1], dp[i-1])

    return max(dp)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(solution(n, arr))