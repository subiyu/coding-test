from collections import deque
import math


def check_P(num):
    if num <= 1:
        return True

    for i in range(2, num):
        if i > int(num ** 0.5):
            break
        if num % i == 0:
            return True
    return False


def trans_k(num, k):
    if num < k:
        return [num]
    stack = deque([])
    result = []

    while k <= num:
        rest = num % k
        stack.append(rest)
        num //= k
    stack.append(num)

    while stack:
        result.append(stack.pop())

    return result


def solution(n, k):
    answer = 0
    n = trans_k(n, k)
    print("n = ", n)
    origin_num = ""

    # 소수 양쪽에 0이 있는 경우, 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    for digit in n:
        if digit == 0:
            if origin_num == '':
                continue
            elif not check_P(int(origin_num)):
                answer += 1
            origin_num = ""
        else:
            origin_num += str(digit)

    # 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    if origin_num != '':
        if not check_P(int(origin_num)):
            answer += 1
    return answer