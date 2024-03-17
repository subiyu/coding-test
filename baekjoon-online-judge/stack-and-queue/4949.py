from collections import deque

def solution(str):
    stack = deque([])
    str_len = len(str)

    last = ''
    for s in str:
        if s == '(' or s == ')' or s == '[' or s == ']':
            st = s
            stack.append(st)
            if last == '(' and st == ')':
                stack.pop()
                stack.pop()
            elif last == '[' and st == ']':
                stack.pop()
                stack.pop()
            if stack:
                last = stack[-1]
            else:
                last = ''

    if stack:
        print("no")
    else:
        print("yes")

input_str = ""

while True:
    input_str = input("")
    if input_str == ".":
        break
    solution(input_str)
