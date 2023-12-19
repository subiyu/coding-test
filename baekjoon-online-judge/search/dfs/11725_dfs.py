import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, parents, start):
    visited[start] = True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            parents[neighbor] = start
            dfs(graph, visited, parents, neighbor)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, visited, parents, 1)

for i in parents[2:]:
    print(i)
