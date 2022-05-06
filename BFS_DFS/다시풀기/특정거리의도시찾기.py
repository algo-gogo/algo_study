########### 특정 기리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# from collections import deque
#
# n, m, k, x = map(int, input().split())
#
# graph = [[] for _ in range(n)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a - 1].append(b - 1)
#
# print(graph)
#
# def bfs(start_city, distance):
#     queue = deque()
#     queue.append((start_city - 1, 0))
#     visited = [False for _ in range(n)]
#
#     result_list = []
#     while queue:
#         city, d = queue.popleft()
#         if d == distance:
#             result_list.append(city)
#         city_list = graph[city]
#         for c in city_list:
#             if not visited[c]:
#                 queue.append((c, d + 1))
#                 visited[c] = True
#
#     return result_list
#
#
# result = bfs(x, k)
# print(result)
# if len(result) == 0:
#     print(-1)
# else:
#     for i in result:
#         print(i + 1)
