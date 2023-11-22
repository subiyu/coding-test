def solution(n):
    answer = 0
    answer = fibo(n) % 1234567
    return answer

def fibo(num):
    dp = [0] * (num + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, num + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[num]