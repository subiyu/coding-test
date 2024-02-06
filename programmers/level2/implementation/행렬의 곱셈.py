def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        row = arr1[i]
        for j in range(len(row)):
            row2 = arr2[j]
            for k in range(len(arr2[0])):
                answer[i][k] += row[j] * row2[k]

    return answer