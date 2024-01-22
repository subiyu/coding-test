from collections import deque

def bfs(graph, visited, parents, node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                parents[neighbor] = node
                visited[neighbor] = True

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, visited, parents, 1)

for i in parents[2:]:
    print(i)