def solution(n, words):
    answer = []
    last = ''
    arr = []
    order = 0

    for i in range(len(words)):
        word = words[i]
        personIdx = i % n + 1  # person 번호
        if i % n == 0:
            order += 1  # 차례 1증가
        first = word[0]  # 첫 글자
        if i != 0 and last != first:  # 0번째 word는 앞글자 무관
            answer.append(personIdx)
            answer.append(order)
            return answer
        else:
            if word in arr:
                answer.append(personIdx)
                answer.append(order)
                return answer
        last = word[-1]  # 다음 단어의 앞글자와 같은지 확인하기 위해 last 정의
        arr.append(word)

    answer = [0, 0]
    return answer