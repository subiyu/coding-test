from collections import deque

def bfs(node, targetNum):
    count = 1
    queue = deque([[node, count]])

    while queue:
        arr = queue.popleft()
        node = arr[0]
        count = arr[1] + 1
        left = node * 2
        right = node * 10 + 1
        if left == targetNum or right == targetNum:
            return count
        if left < targetNum:
            queue.append([left, count])
        if right < targetNum:
            queue.append([right, count])

    return -1

A, B = map(int, input().split(" "))
print(bfs(A, B))