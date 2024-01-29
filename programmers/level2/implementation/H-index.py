def solution(citations):
    answer = 0

    for h in range(max(citations)):
        if h <= answer:
            continue
        count = 0
        for citation in citations:
            if citation >= h:
                count += 1
        if count >= h:
            answer = h

    return answer