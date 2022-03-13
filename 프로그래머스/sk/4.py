# from itertools import permutations
#
#
# def bfs(start, end, n, graph):
#     root = [start]
#     visited = [0] * (n + 1)
#     way = [0] * (n + 1)
#     while root:
#         k = root.pop()
#         if k == end:
#             break
#         if visited[k] == 0:
#             visited[k] = 1
#             for i in graph[k]:
#                 root.append(i[0])
#                 way[i[0]] = way[k] + i[1]
#     return way[end]
#
#
# def solution(n, edges):
#     graph = [[] for _ in range(n + 1)]
#
#     for i in range(len(edges)):
#         x = edges[i][0]
#         y = edges[i][1]
#         graph[x].append([y, 1])
#
#     p_list = list(permutations(range(n), 3))
#
#     result = 0
#     for p in p_list:
#         way1 = bfs(p[0], p[1], n, graph)
#         way2 = bfs(p[1], p[2], n, graph)
#         way3 = bfs(p[0], p[2], n, graph)
#         print(way1, way2, way3)
#         if way1 + way2 == way3:
#             result += 1
#
#     return result
#
#
# print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))

def solution(n, clockwise):
    return 2 ** (n - 1)

print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))
