import heapq, sys

N = int(input())
input = sys.stdin.readline
heap_list = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap_list:
            print(0)
        else:
            result, minus_sign = heapq.heappop(heap_list)
            print(minus_sign)
    else:
        heapq.heappush(heap_list, (abs(x), x))