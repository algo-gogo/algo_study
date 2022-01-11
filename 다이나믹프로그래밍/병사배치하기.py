# https://www.acmicpc.net/problem/18353

n = int(input())

nList = list(map(int, input().split()))

d = [1 for _ in range(n)]

print(d)

for i in range(n):
    for j in range(i):
        if nList[j] > nList[i]:
            d[i] = max(d[j], d[j] + 1)

print(n - max(d))


# 7
# 15 11 4 8 5 2 4