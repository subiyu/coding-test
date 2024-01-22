from collections import deque
import copy

def bfs(heights, size, maxHeight):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([])
    maxCount = 0

    for N in range(maxHeight):
        arr = copy.deepcopy(heights)
        count = 0
        for i in range(size):
            for j in range(size):
                if arr[i][j] > N:
                    queue.append((i, j))
                    arr[i][j] = 0
                    while queue:
                        y, x = queue.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx < 0 or nx >= size or ny < 0 or ny >= size or arr[ny][nx] <= N:
                                continue
                            else:
                                arr[ny][nx] = 0
                                queue.append((ny, nx))
                    count += 1

        if maxCount < count:
            maxCount = count

    return maxCount


N = int(input())
heights = []
maxHeight = 0

for _ in range(N):
    arr = list(map(int, input().split(" ")))
    m = max(arr)
    if maxHeight < m:
        maxHeight = m
    heights.append(arr)

print(bfs(heights, N, maxHeight))