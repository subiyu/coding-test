def solution(r, s):
    str = ""
    for c in s:
        for _ in range(r):
            str += c
    print(str)

    return 0

T = int(input())

for _ in range(T):
    tmp = input().split(" ")
    R = int(tmp[0])
    S = tmp[1]
    solution(R, S)