from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    def bfs(arr, visited, start, target):
        visited[start] = True
        c = 0
        queue = deque([(start, 0)])

        while queue:
            node, c = queue.popleft()
            if node != 0 and words[node-1] == target:
                return c
            for neighbor in arr[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, c + 1))

    def check_diff(str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1

        if count == (len(str1) - 1):
            return True
        else:
            return False

    graph = [[] for _ in range(len(words) + 1)]
    visited = [False] * (len(words) + 1)

    for i in range(len(words) + 1):
        if i == 0:
            t = begin
        else:
            t = words[i - 1]
        for j in range(1, len(words) + 1):
            if i == j:
                continue
            check = words[j - 1]
            if check_diff(t, check):
                graph[i].append(j)

    answer = bfs(graph, visited, 0, target)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))