from collections import deque


def solution(s):
    answer = 0

    for i in range(0, len(s)):  # x
        stack = deque()
        tmp = []
        first_idx = i
        for j in range(len(s)):
            next = j + i
            if next >= len(s):
                next -= len(s)
            tmp.append(s[next])

        before = ""
        for k in range(len(s)):
            current = tmp[k]
            stack.append(current)
            if before == "(" and current == ")":
                stack.pop()
                stack.pop()
            elif before == "[" and current == "]":
                stack.pop()
                stack.pop()
            elif before == "{" and current == "}":
                stack.pop()
                stack.pop()

            if stack:
                before = stack[-1]
            else:
                before = ""

        if not stack:
            answer += 1

    return answer