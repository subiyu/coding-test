import sys
input = sys.stdin.readline

N = int(input())
An = list(map(int, input().split(" ")))
M = int(input())
arr = list(map(int, input().split(" ")))
dic = {}
result = []

for num in An:
    if not num in dic.keys():
        dic[num] = 1
    else:
        dic[num] += 1

for check_num in arr:
    if not check_num in dic.keys():
        result.append(0)
    else:
        result.append(dic[check_num])

print(' '.join(map(str, result)))