def solution(want, number, discount):
    answer = 0
    auth = 10
    dic = {}
    start_idx = 0

    for w in want:
        dic[w] = 0

    for product in discount[:auth]:
        if product in dic:
            dic[product] += 1
        else:
            dic[product] = 1

    for _ in range(len(discount) - auth + 1):
        end_idx = start_idx + auth - 1

        if start_idx != 0:
            pre = discount[start_idx - 1]
            new = discount[end_idx]

            if new not in dic:
                dic[new] = 0

            dic[pre] -= 1
            dic[new] += 1

        for i in range(len(want)):
            w = want[i]
            target = number[i]
            if dic[w] < target:
                break
            else:
                if i == (len(want) - 1):
                    answer += 1

        start_idx += 1

    return answer