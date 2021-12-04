# n X m
# 0 빈칸
# 1 벽
# 2 바이러스
# 벽을 3개 세워서 안전영역의 최댓값

from itertools import combinations

n, m = map(int, input().split())

array = []
for i in range(n):
    l = list(map(int, input().split()))
    array.append(l)

print(array)
zeroList = []

# for i in range(n):
#     for j in range(m):
#         if array[i][j] == 0:
#             zeroList.append((i, j))
#
# print(zeroList)
# selectZero = list(combinations(zeroList, 3))
# print(selectZero)


def dfs(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        if array[x][y] == 0:
            array[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return 1
        else:
            return 0
    return 0

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            now = 0
            count += 1

