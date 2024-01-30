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

6. 2차원 배열에서 최댓값 찾기

    maxVal = max(max(row) for row in graph)

7. stack 비어있는지 확인

   if not stack:

8. 딕셔너리

   dic = {}
   
   dic['apple'] = 1

9. deque 초기화

   queue = deque([(0, 0)])

10. 해쉬(if target in arr) => 여기서 arr을 배열으로 만드는 것 보다 해쉬로 만드는게 효율성이 좋음(검색 속도 차이) 

    hash_set = set()

    hash_set.add(1)
