def solution(sticker):
    if len(sticker) == 1:  # 스티커가 한 장일 경우
        return sticker[0]

    # 첫 번째 스티커를 선택한 경우
    dp_first = [0] * len(sticker)
    dp_first[0] = sticker[0]
    dp_first[1] = dp_first[0]
    for i in range(2, len(sticker) - 1):
        dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + sticker[i])

    # 첫 번째 스티커를 선택하지 않은 경우
    dp_second = [0] * len(sticker)
    dp_second[0] = 0
    dp_second[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp_second[i] = max(dp_second[i - 1], dp_second[i - 2] + sticker[i])

    # 마지막 스티커를 선택한 경우
    dp_last = [0] * len(sticker)
    dp_last[0] = 0
    dp_last[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp_last[i] = max(dp_last[i - 1], dp_last[i - 2] + sticker[i])

    # 최대값을 리턴
    return max(max(dp_first), max(dp_second), max(dp_last))

# 예시
sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))  # 출력: 36
