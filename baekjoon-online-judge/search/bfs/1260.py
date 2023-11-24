from collections import deque

def dfs(graph, visited, start):
    visited[start] = True
    result.append(start)

    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

N, M, V = map(int, input().split(" "))
graph = {i: [] for i in range(N+1)}

for i in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = []
dfs(graph, visited, V)
print(' '.join(map(str, result)))

visited = [False] * (N+1)
result = []
bfs(graph, visited, V)
print(' '.join(map(str, result)))