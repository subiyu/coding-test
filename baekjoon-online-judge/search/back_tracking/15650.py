def back_tracking(n, m, result, visited):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if result:
            if result[-1] >= i:
                continue
        if not visited[i]:
            result.append(i)
            visited[i] = True
            back_tracking(n, m, result, visited)
            result.pop()
            visited[i] = False

N, M = map(int, input().split(" "))
visited = [False] * (N+1)
result = []
back_tracking(N, M, result, visited)