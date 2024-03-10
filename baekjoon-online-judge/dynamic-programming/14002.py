#14002
import copy

def solution(n, numbers):
    dp = [[0, []] for _ in range(n+1)]
    dp[1] = [1, [numbers[0]]]

    for i in range(2, n+1):
        tmp = []
        tmp2 = []
        tmp3 = []
        for j in range(1, i):
            if numbers[i-1] > numbers[j-1]:
                tmp.append(dp[j][0])
                tmp2.append(dp[j][1])
        if not tmp:
            dp[i] = [1, [numbers[i-1]]]
        else:
            maxVal = max(tmp)
            maxIdx = tmp.index(maxVal)
            tmp3 = copy.deepcopy(tmp2[maxIdx])
            tmp3.append(numbers[i-1])
            dp[i] = [maxVal + 1, tmp3]

    max_len, result = max(dp, key=lambda x:x[0])
    print(max_len)
    print(' '.join(map(str, result)))

    return 0

N = int(input())
arr = list(map(int, input().split(" ")))

solution(N, arr)