def backtracking(arr, depth, visited, result, answer):
    if depth == M:
        answer.append(tuple(result))
        return

    for i in range(len(arr)):
        if result and depth > 0:
            if result[depth-1] > arr[i]:
                continue
        if not visited[i]:
            visited[i] = True
            result[depth] = arr[i]
            backtracking(arr, depth + 1, visited, result, answer)
            visited[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))

visited = [False] * N
result = [0] * M
answer = []
arr.sort()

backtracking(arr, 0, visited, result, answer)
unique_answer = list(set(answer))
unique_answer.sort()

for seq in unique_answer:
    print(' '.join(map(str, seq)))