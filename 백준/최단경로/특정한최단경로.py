# import heapq
# import sys
#
# # 노드의 개수와 간선의 개수
# n, m = map(int, sys.stdin.readline().split())
#
# INF = int(1e9)
# graph = [[] for i in range(n + 1)]
#
# for _ in range(m):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a].append((b, c))
#
# v1, v2 = map(int, sys.stdin.readline().split())
#
#
# def dijkstra(start):
#     distance = [INF] * (n + 1)
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#     return distance
#
#
# # dijkstra(1)
# # result = distance[v1]
# # result2 = distance[v2]
# #
# # dijkstra(v1)
# # result += distance[v2]
# # result2 += distance[n]
# #
# # dijkstra(v2)
# # result += distance[n]
# # result2 += distance[v1]
# #
# # print(min(result,result2))
# #
# one = dijkstra(1)
# v1_d = dijkstra(v1)
# v2_d = dijkstra(v2)
#
# v1FirstRoute = one[v1] + v1_d[v2] + v2_d[n]
# v2FirstRoute = one[v2] + v2_d[v1] + v1_d[n]
#
# result = min(v1FirstRoute, v2FirstRoute)
# print(result if result < INF else -1)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))


def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance


v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)