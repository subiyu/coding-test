N = int(input())
cards = set(map(int, input().split(" ")))
M = int(input())
numbers = list(map(int, input().split(" ")))
result = []

for number in numbers:
    if number in cards:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))