from collections import deque

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

circular_queue = deque([i for i in range(1, N+1)])
idx = 0
count = 0

for num in arr:
    len_queue = len(circular_queue)
    if circular_queue[0] != num:
        for i in range(len_queue):
            if circular_queue[i] == num:
                idx = i
                break
        if idx <= (len_queue // 2): #왼쪽으로
            while(circular_queue[0] != num):
                circular_queue.append(circular_queue.popleft())
                count += 1
        else:
            while (circular_queue[0] != num):
                circular_queue.appendleft(circular_queue.pop())
                count += 1
    circular_queue.popleft()

print(count)