# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    matrix[m1][m2] = matrix[m2][m1] = 1

print(matrix)

def bfs(start):
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(matrix[start])):
            if matrix[v][w] == 1 and (w not in visited):
                visited.append(w)
                queue.append(w)

def dfs(start, visited=[]):
    visited.append(start)
    print(start, end=' ')

    for w in range(len(matrix[start])):
        if matrix[start][w] == 1 and (w not in visited):
            dfs(w, visited)

dfs(v)
print()
bfs(v)


# from sys import stdin
# from collections import deque
#
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v+1, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# n, m, v = map(int, stdin.readline().split())
# matrix = [[0] for _ in range(m)]
# # [[0], [0], [0], [0], [0]]
# for i in range(len(matrix)):
#     a, b = map(int, input().split())
#     matrix[i][0] = a
#     matrix[i].append(b)
#
# print(matrix)
#
# visitedDfs = [False] * len(matrix)
# visitedBfs = [False] * len(matrix)
#
# dfs(matrix, 0, visitedDfs)
# print()
# bfs(matrix, 1, visitedBfs)
