def solution(n, numbers):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        tmp = []
        for j in range(i-1, -1, -1):
            if numbers[i-1] < numbers[j-1]:
                tmp.append(dp[j])
        if not tmp:
            tmp.append(0)
        dp[i] = max(tmp) + 1

    return max(dp)

N = int(input())
arr = list(map(int, input().split(" ")))

print(solution(N, arr))