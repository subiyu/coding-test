N = int(input())
An = set(map(int, input().split(" ")))
M = int(input())
X_list = list(map(int, input().split(" ")))

for num in X_list:
    if num in An:
        print(1)
    else:
        print(0)