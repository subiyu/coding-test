from collections import deque

def bfs(graph, visited, node):
    result = 0
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                result += 1
                queue.append(neighbor)
                visited[neighbor] = True

    return result

numCom = int(input())
numPair = int(input())
graph = [[] for _ in range(numCom+1)]
visited = [False] * (numCom+1)

for _ in range(numPair):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, visited, 1))