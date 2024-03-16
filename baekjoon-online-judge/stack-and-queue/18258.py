from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    str = sys.stdin.readline().strip().split(" ")
    if len(str) == 2:
        queue.append(str[1])
    else:
        str = str[0]
        if str == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif str == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif str == "size":
            print(len(queue))
        elif str == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif str == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)