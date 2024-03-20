N, M = map(int, input().split(" "))
set_s = set()
count = 0

for _ in range(N):
    set_s.add(input())

for _ in range(M):
    if input() in set_s:
        count += 1

print(count)