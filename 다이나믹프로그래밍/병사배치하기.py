# https://www.acmicpc.net/problem/18353

n = int(input())

nList = list(map(int, input().split()))

d = [0] * n

print(d)

count = 0

for i in range(n - 1):
    if nList[i] < nList[i + 1]:
        count += 1

print(count)