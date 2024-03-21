def back_tracking(n, m, result, visited):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in arr:
        if not visited[i]:
            result.append(i)
            visited[i] = True
            back_tracking(n, m, result, visited)
            result.pop()
            visited[i] = False

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr = sorted(arr)
visited = [False] * (max(arr)+1)
result = []
back_tracking(N, M, result, visited)