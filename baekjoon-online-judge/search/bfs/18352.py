from collections import deque
import sys

def dfs(graph, visited, start, count, target):
    result = []
    queue = deque([[start, count]])

    while queue:
        node, count = queue.popleft()
        if count == target:
            result.append(node)
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append([neighbor, count+1])
                visited[neighbor] = True

    if not result:
        print(-1)
    else:
        result = sorted(result)
        [print(value) for value in result]

N, M, K, X = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split(" "))
    graph[A].append(B)

dfs(graph, visited, X, 0, K)