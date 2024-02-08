def solution(s):
    answer = []
    last_element = []

    # 중괄호를 제거하고 숫자들을 추출하여 2차원 배열 생성
    arr = []
    filtered_s = s.lstrip('{').rstrip('}').split("},{")
    for element in filtered_s:
        arr.append([int(element) for element in element.split(",")])

    for i in range(1, len(arr) + 1):
        for check_set in arr:
            if len(check_set) == i:
                for j in range(len(check_set)):
                    if check_set[j] not in last_element:
                        answer.append(check_set[j])
                        last_element.append(check_set[j])

    return answer


# # 더 쉬운 풀이
# import re
# from collections import Counter
#
#
# def solution(s):
#     dic = Counter(re.findall('\d+', s))
#
#     return list(map(int, [k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)]))