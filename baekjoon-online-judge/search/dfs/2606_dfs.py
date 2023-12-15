def dfs(graph, visited, start):
    visited[start] = True
    count = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)

    return count

numCom = int(input())
numPair = int(input())
graph = [[] for _ in range(numCom+1)]
visited = [False] * (numCom+1)

for _ in range(numPair):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

result = 0
print(dfs(graph, visited, 1)-1)