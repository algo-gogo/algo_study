# # https://www.acmicpc.net/problem/14502
# # n X m
# # 0 빈칸
# # 1 벽
# # 2 바이러스
# # 벽을 3개 세워서 안전영역의 최댓값
#
# from itertools import combinations
# import copy
#
# n, m = map(int, input().split())
#
# array = []
# arrayCopy = [[0] * m for _ in range(n)]
# for i in range(n):
#     l = list(map(int, input().split()))
#     array.append(l)
#
# print(array)
# # virus 퍼져나가게
#
# # dx = [-1, 0, 1, 0]
# # dy = [0, 1, 0, -1]
# # def virus(x, y):
# #     for i in range(4):
# #         nx = x + dx[i]
# #         ny = y + dy[i]
# #         if nx >= 0 and nx < n and ny >= 0 and ny < m:
# #             if arrayCopy[nx][ny] == 0:
# #                 arrayCopy[nx][ny] = 2
# #                 virus(nx, ny)
# #
# #
# # def dfs(x, y):
# #     if 0 <= x < n and 0 <= y < m:
# #         if arrayCopy[x][y] == 0:
# #             arrayCopy[x][y] = 2
# #             dfs(x - 1, y)
# #             dfs(x + 1, y)
# #             dfs(x, y - 1)
# #             dfs(x, y + 1)
# #
# #
# # def findSafe():
# #     score = 0
# #     for i in range(n):
# #         for j in range(m):
# #             if arrayCopy[i][j] == 0:
# #                 score += 1
# #     return score
# #
# #
# # result = 0
# #
# #
# # def wallSelect(count):
# #     global result
# #     # 벽이 3개인 경우
# #     if count == 3:
# #         for i in range(n):
# #             for j in range(m):
# #                 arrayCopy[i][j] = array[i][j]
# #         for i in range(n):
# #             for j in range(m):
# #                 if arrayCopy[i][j] == 2:
# #                     virus(i, j)
# #         result = max(result, findSafe())
# #         return
# #     else:
# #         for i in range(n):
# #             for j in range(m):
# #                 if array[i][j] == 0:
# #                     array[i][j] = 1
# #                     count += 1
# #                     wallSelect(count)
# #                     array[i][j] = 0
# #                     count -= 1
# #
# #
# # wallSelect(0)
# # print(result)
#
#
# ##############################################
#
# zeroList = []
# for i in range(n):
#     for j in range(m):
#         if array[i][j] == 0:
#             zeroList.append((i, j))
#
# print(zeroList)
# selectZero = list(combinations(zeroList, 3))
#
#
# # print(selectZero)
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
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if arrayCopy[nx][ny] == 0:
#                 arrayCopy[nx][ny] = 2
#                 virus(nx, ny)
#
#
# resultList = []
# for zeroList in selectZero:
#     arrayCopy = copy.deepcopy(array)
#     for x, y in zeroList:
#         arrayCopy[x][y] = 1
#
#     for i in range(n):
#         for j in range(m):
#             if arrayCopy[i][j] == 2:
#                 virus(i, j)
#     resultList.append(findSafe())
#
# print(max(resultList))


from collections import deque
from itertools import combinations
import copy

# n, m = map(int, input().split())
n, m = 4, 4

graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
graph.append([0, 0, 1, 1])
graph.append([0, 0, 1, 0])
graph.append([1, 1, 0, 0])
graph.append([0, 2, 0, 1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zero_place = []
for i, i_val in enumerate(graph):
    for j, j_val in enumerate(i_val):
        if j_val == 0:
            zero_place.append([i, j])

zero_combi = list(combinations(zero_place, 3))


def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    while queue:
        print(queue)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 2:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))


def findSafe(graph):
    cnt = 0
    for i in graph:
        for j in i:
            if j == 0:
                cnt += 1

    print(cnt)
    for i in graph:
        print(i)
    print()
    return cnt


answer_lst = []

for i in zero_combi:
    print("i", i)
    temp_graph = copy.deepcopy(graph)
    temp_graph[i[0][0]][i[0][1]] = 1
    temp_graph[i[1][0]][i[1][1]] = 1
    temp_graph[i[2][0]][i[2][1]] = 1

    # print(temp_graph)

    a, b = -1, -1
    for i, i_val in enumerate(temp_graph):
        for j, j_val in enumerate(i_val):
            if j_val == 2:
                a, b = i, j
                bfs(a, b, temp_graph)

    answer_lst.append(findSafe(temp_graph))
    continue

print(max(answer_lst))

# print(len(zero_combi))
# print(answer_lst)