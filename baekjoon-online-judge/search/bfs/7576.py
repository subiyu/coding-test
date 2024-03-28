from collections import deque
def bfs(arr, n, m):
    queue = deque([])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    day = 0

    #0일 일때, 익은 토마토 체크
    for p in range(n):
        for q in range(m):
            if arr[p][q] == 1:
                queue.append((p, q, day))

    while queue:
        y, x, d = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif arr[ny][nx] == 0:
                arr[ny][nx] = 1
                queue.append((ny, nx, d+1))

    for p in range(n):
        for q in range(m):
            if arr[p][q] == 0:
                return -1

    return d

M, N = map(int, input().split(" "))
arr = []

for i in range(N):
    arr.append(list(map(int, input().split(" "))))

print(bfs(arr, N, M))