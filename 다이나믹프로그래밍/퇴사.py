# https://www.acmicpc.net/problem/14501
n = int(input())
nList = []

for i in range(n):
    l = list(map(int, input().split()))
    nList.append(l)

print(nList)

d = [0 for i in range(n)]
print(d)

length = len(nList)

for i in range(len(nList) - 1, 0, -1):
    for j in range(len(nList) - i):
        if nList[length - j - 1][0] <= j + 1:
            d[j] = max(d[j])
