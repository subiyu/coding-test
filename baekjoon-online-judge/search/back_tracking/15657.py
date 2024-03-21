def back_tracking(n, m, result, visited, i):
    if len(result) == m:
        print(' '.join(map(str, result)))
        visited[i] = True
        return

    for i in arr:
        if result:
            if result[-1] > i:
                continue
        if not visited[i]:
            result.append(i)
            back_tracking(n, m, result, visited, i)
            result.pop()
            visited[i] = False

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr = sorted(arr)
visited = [False] * (max(arr)+1)
result = []
back_tracking(N, M, result, visited, 0)