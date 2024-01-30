from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])

    while queue:
        node, depth = queue.popleft()

        if depth == len(numbers):
            if node == target:
                answer += 1
            continue

        left = node - numbers[depth]
        right = node + numbers[depth]
        queue.append((left, depth + 1))
        queue.append((right, depth + 1))

    return answer