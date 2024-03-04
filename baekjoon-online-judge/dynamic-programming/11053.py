def solution(n, numbers):
    dp = [0] * (n+1)
    if n == 1:
        return 1

    dp[1] = 1
    for i in range(2, n+1):
        num = numbers[i-1]
        arr = []
        for k in range(i - 1, -1, -1):
            if numbers[k - 1] < num:
                arr.append(dp[k])
            if k == 0:
                dp[i] = 1
        if arr:
            dp[i] = max(arr) + 1

    return max(dp)

N = int(input())
arr = list(map(int, input().split(" ")))
print(solution(N, arr))