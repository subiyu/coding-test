from collections import deque

def solution(s):
    answer = True
    stack = deque()
    last = ""

    for bracket in s:
        stack.append(bracket)
        if(last == "(" and bracket == ")"):
            stack.pop()
            stack.pop()
            if stack:
                last = stack[-1]
                continue
        last = bracket

    if not stack:
        return True
    else:
        return False