from collections import deque

def solution(m, arr):
    queue = deque([(p, i) for i, p in enumerate(arr)])

    # 중요도가 높을수록 우선순위(max-heap)
    count = 1
    while queue:
        p, i = queue.popleft()
        if any(p < q[0] for q in queue):
            queue.append((p, i))
        else:
            if i == m:
                return count
            count += 1

T = int(input())

for _ in range(T):
    N, M = map(int, input().split(" "))
    p_list = list(map(int, input().split(" ")))
    print(solution(M, p_list))