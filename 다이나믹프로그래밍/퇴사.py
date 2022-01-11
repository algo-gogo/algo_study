# https://www.acmicpc.net/problem/14501
n = int(input())
nList = []

for i in range(n):
    l = list(map(int, input().split()))
    nList.append(l)

print(nList)

d = [[] for i in range(n)]
print(d)

for i in range(len(nList) - 1, 0, -1):
    for j in range(len(d)):
        nList[i][0]