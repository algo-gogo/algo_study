# https://www.acmicpc.net/problem/14502
# n X m
# 0 빈칸
# 1 벽
# 2 바이러스
# 벽을 3개 세워서 안전영역의 최댓값

from itertools import combinations
import copy

n, m = map(int, input().split())

array = []
arrayCopy = [[0] * m for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    array.append(l)

print(array)
# virus 퍼져나가게

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if arrayCopy[nx][ny] == 0:
#                 arrayCopy[nx][ny] = 2
#                 virus(nx, ny)
#
#
# def dfs(x, y):
#     if 0 <= x < n and 0 <= y < m:
#         if arrayCopy[x][y] == 0:
#             arrayCopy[x][y] = 2
#             dfs(x - 1, y)
#             dfs(x + 1, y)
#             dfs(x, y - 1)
#             dfs(x, y + 1)
#
#
# def findSafe():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if arrayCopy[i][j] == 0:
#                 score += 1
#     return score
#
#
# result = 0
#
#
# def wallSelect(count):
#     global result
#     # 벽이 3개인 경우
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 arrayCopy[i][j] = array[i][j]
#         for i in range(n):
#             for j in range(m):
#                 if arrayCopy[i][j] == 2:
#                     virus(i, j)
#         result = max(result, findSafe())
#         return
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if array[i][j] == 0:
#                     array[i][j] = 1
#                     count += 1
#                     wallSelect(count)
#                     array[i][j] = 0
#                     count -= 1
#
#
# wallSelect(0)
# print(result)


##############################################

zeroList = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            zeroList.append((i, j))

print(zeroList)
selectZero = list(combinations(zeroList, 3))


# print(selectZero)


def findSafe():
    score = 0
    for i in range(n):
        for j in range(m):
            if arrayCopy[i][j] == 0:
                score += 1
    return score


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arrayCopy[nx][ny] == 0:
                arrayCopy[nx][ny] = 2
                virus(nx, ny)


resultList = []
for zeroList in selectZero:
    arrayCopy = copy.deepcopy(array)
    for x, y in zeroList:
        arrayCopy[x][y] = 1

    for i in range(n):
        for j in range(m):
            if arrayCopy[i][j] == 2:
                virus(i, j)
    resultList.append(findSafe())

print(max(resultList))
