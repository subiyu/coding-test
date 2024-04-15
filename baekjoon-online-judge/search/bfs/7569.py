from collections import deque

def check_tomato(arr, M, N, H):
    result = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    result.append((k, j, i, 0))

    return result
def bfs(arr, M, N, H):
    queue = deque([])
    queue.extend(check_tomato(arr, M, N, H))
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    day = 0

    while queue:
        x, y, z, d = queue.popleft()
        day = max(day, d)

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H or arr[nz][ny][nx] == -1:
                continue
            elif arr[nz][ny][nx] == 0:
                queue.append((nx, ny, nz, d+1))
                arr[nz][ny][nx] = 1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1

    return day


M, N, H = map(int, input().split(" "))
tomatoes = [[[] for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomatoes[i][j] = list(map(int, input().split(" ")))

print(bfs(tomatoes, M, N, H))
