import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
deque = deque([])

for _ in range(N):
    arr = input().strip().split(" ")
    if len(arr) == 2:
        if arr[0] == "push_front":
            deque.appendleft(arr[1])
        elif arr[0] == "push_back":
            deque.append(arr[1])
    else:
        arr = arr[0]
        if arr == "pop_front":
            if deque:
                print(deque.popleft())
            else:
                print(-1)
        elif arr == "pop_back":
            if deque:
                print(deque.pop())
            else:
                print(-1)
        elif arr == "size":
            print(len(deque))
        elif arr == "empty":
            if deque:
                print(0)
            else:
                print(1)
        elif arr == "front":
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif arr == "back":
            if deque:
                print(deque[-1])
            else:
                print(-1)
