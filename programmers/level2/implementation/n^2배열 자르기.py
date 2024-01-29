def solution(n, left, right):
    arr = []

    for i in range(left, right+1):
        if (i%n) <= (i//n):
            arr.append((i//n)+1)
        else:
            arr.append((i%n)+1)

    return arr