# https://www.acmicpc.net/problem/14501

n = int(input())

work_list = []

for i in range(n):
    a, b = map(int, input().split())
    work_list.append([a, b])

print(work_list)

d = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + work_list[i][0] > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(work_list[i][1] + d[i + work_list[i][0]], d[i + 1])

print(d[0])

