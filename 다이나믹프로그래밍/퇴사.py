# https://www.acmicpc.net/problem/14501
n = int(input())
nList = []

for i in range(n):
    l = list(map(int, input().split()))
    nList.append(l)

print(nList)

d = [[0] for i in range(n)]
print(d)