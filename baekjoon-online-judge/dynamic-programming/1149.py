def solution(n, arr):
    for i in range(1, n):
        arr[i][0] += min(arr[i-1][1], arr[i-1][2]) #Red 선택
        arr[i][1] += min(arr[i-1][0], arr[i-1][2]) #Green 선택
        arr[i][2] += min(arr[i-1][0], arr[i-1][1]) #Blue 선택

    return min(arr[-1])

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

print(solution(N, arr))