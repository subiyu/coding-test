from collections import deque
def bfs(n, arr, row, col, visited):
    color = arr[row][col]
    queue = deque([(row, col)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif arr[ny][nx] == color and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

def bfs2(n, arr, row, col, visited):
    color = arr[row][col]
    queue = deque([(row, col, color)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        y, x, c = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx]:
                continue
            elif c == 'B':
                if arr[ny][nx] == c:
                    visited[ny][nx] = True
                    queue.append((ny, nx, color))
            elif c == 'R':
                if arr[ny][nx] == c or arr[ny][nx] == 'G':
                    visited[ny][nx] = True
                    queue.append((ny, nx, arr[ny][nx]))
            elif c == 'G':
                if arr[ny][nx] == c or arr[ny][nx] == 'R':
                    visited[ny][nx] = True
                    queue.append((ny, nx, arr[ny][nx]))

N = int(input())
colors = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]
count1 = 0
count2 = 0

for i in range(N):
    tmp = input()
    for j in range(N):
        colors[i][j] = tmp[j]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count1 += 1
            visited[i][j] = True
            bfs(N, colors, i, j, visited)
        if not visited2[i][j]:
            count2 += 1
            visited2[i][j] = True
            bfs2(N, colors, i, j, visited2)

print(count1, count2)