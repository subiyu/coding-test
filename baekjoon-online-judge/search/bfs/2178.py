from collections import deque

def bfs(maze, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i] #+x는 오른쪽 방향
            ny = y + dy[i] #+y는 밑쪽 방향

            if nx < 0 or nx >= M or ny < 0 or ny >= N or maze[ny][nx] == 0: #maze[ny][nx] == 0 이면 이미 방문한 노드로 간주
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]

N, M = map(int, input().split(" "))
maze = []

for _ in range(N):
    maze.append(map(int, list(input())))

print(bfs(maze, N, M))