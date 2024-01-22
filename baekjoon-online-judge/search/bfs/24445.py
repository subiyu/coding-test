from collections import deque
import sys

def bfs(graph, visited, start):
    result = [0] * len(graph)
    count = 1
    queue = deque([start])
    visited[start] = True
    result[start] = count

    while queue:
        node = queue.popleft()
        for neighbor in sorted(graph[node], reverse=True):
            if not visited[neighbor]:
                count += 1
                queue.append(neighbor)
                visited[neighbor] = True
                result[neighbor] = count

    return result

N, M, R = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)

arr = bfs(graph, visited, R)

[print(i) for i in arr[1:]]