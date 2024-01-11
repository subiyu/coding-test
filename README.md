# coding-test
코딩 테스트 문제를 풀이한 코드를 업로드하는 저장소

# 오답 원인 목록
1. list = sorted(list)

2. 내림차순 정렬 sorted(arr, reverse=True)

3. 리스트 컴프리헨션 [print(value) for value in result]

4. 입력값이 10221 일때 [1, 0, 2, 2, 1]로 변환하기

    list(input) => ['1', '0', '2', '2', '1']

    map(int, list(input()) => [1, 0, 2, 2, 1]

    map은 key, value 쌍이므로 인덱싱 불가능

    maze = map(int, list(input()) 일 때, maze[1][1] 접근 불가능

    => 다시 list로 감싼다

    => list(map(int, list(input())))

5. 깊은복사

    import copy

    arr2 = copy.deepcopy(arr)
