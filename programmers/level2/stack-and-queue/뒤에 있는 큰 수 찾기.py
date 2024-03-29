def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            last = stack.pop()
            answer[last] = numbers[i]

        stack.append(i)

    return answer