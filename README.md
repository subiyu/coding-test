# coding-test
코딩 테스트 문제를 풀이한 코드를 업로드하는 저장소

# 오답 원인 목록
0-1. sys.stdin.readline()

=> 개행문자('\n') 없애기: sys.stdin.readline().strip()

0-2. sys.setrecursionlimit(10**6)

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

11. 아스키코드표

    65~90: 대문자
    
    97~122: 소문자

12. Counter()

    from collections import Counter
    
    dic = Counter(re.findall('\d+', s)

13. dictionary의 value를 기준으로 오름차순 정렬하여 리스트로 반환

    list(map(int, [k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)]))


    s = "2 10 12 > 3 9 6"

14. s = "{{2},{2,1},{2,1,3},{2,1,3,4}}" 일 때 int형 2차원 배열로 만들기

    s = s.split("},{") arr = []
    
    for element in s:
    
    arr.append(list(map(int, re.findall('\d+', element))))


15. s = "2 10 12 > 3 9 6" 일 때, [2, 10, 12], '>', [3, 9, 6] 으로 만들기

    pattern = r"(\d+ \d+ \d+) ([><=]) (\d+ \d+ \d+)"
      
    match = re.match(pattern, s)

    if match:

    left = list(map(int, match.group(1).split()))

16. enumerate()

    queue = deque([(i,v) for i,v in enumerate(priorities)])

17. 정규표현식을 사용하여 알파벳이 아닌 문자 찾기
    
    non_alphabet_pattern = re.compile('[^a-zA-Z]')
    
    result = bool(non_alphabet_pattern.search(s))

20. 삼항연산자

    max_count = count if max_count < count else max_count

21. 우선순위 큐

    import heapq

    heap_list = []
    
    heapq.heappush(heap_list, 2)

    heapq.heappop(heap_list) #최소값 삭제

    heapq.heapify(arr) #리스트를 힙으로 변환

    

23. 리스트 붙이기([1, 2, 3]을 123으로 출력
    
    arr = [1, 2, 3]
    
    print(''.join(map(str, arr)))
