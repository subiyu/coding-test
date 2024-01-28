from collections import deque


def solution(maps):
    answer = 0
    row_num = len(maps)
    col_num = len(maps[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque([(0, 0)])

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx < 0 or nx >= col_num or ny < 0 or ny >= row_num:
                continue
            elif maps[ny][nx] == 1:
                maps[ny][nx] += maps[cy][cx]
                queue.append((nx, ny))

    answer = maps[row_num - 1][col_num - 1]

    if answer == 1:
        return -1
    else:
        return answer