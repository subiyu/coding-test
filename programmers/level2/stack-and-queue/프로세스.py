# priority이 클수록 우선순위가 높다, Queue는 FIFO
def solution(priorities, location):
    answer = 0
    count = 0
    idx = location

    while priorities:
        maxPri = max(priorities)
        selected_process = priorities[0]

        if selected_process < maxPri:
            if count == idx:
                idx += len(priorities)
            priorities.append(selected_process)
        else:
            answer += 1
            if count == idx:
                return answer

        priorities.pop(0)
        count += 1

    return answer