from collections import deque

def solution(str):
    stack = deque([])
    str_len = len(str)

    last = ''
    for i in range(str_len):
        st = str[i]
        stack.append(st)
        if last == '(' and st == ')':
            stack.pop()
            stack.pop()
        if stack:
            last = stack[-1]
        else:
            last = ''

    if stack:
        print("NO")
    else:
        print("YES")

T = int(input())
for _ in range(T):
    solution(input(""))