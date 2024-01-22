def solution(arr):
    answer = 0
    arr = sorted(arr)
    i = 1
    while True:
        num = arr[-1] * i
        for v in arr[0:len(arr)-1]:
            if num % v != 0:
                i += 1
                break
            if v == arr[len(arr)-2]:
                return num

    return answer