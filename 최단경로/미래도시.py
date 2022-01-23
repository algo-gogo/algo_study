# A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매
# 연결된 곳은 양방향으로 이동가능
# 소개팅 상대는 k번 회사에 존재한다. A는 X번 회사에 가서 물건을 판매하기 전에 커피마시러 방문
# 결국 A는 1번 회사에서 출발해서 K번 회사를 방문한 뒤 X번 회사로 가는것이 목표

# 입력: 회사의 개수 N, 경로의 개수 M
# 연결된 두 회사의 번호가 공백으로 구분
#

# INF = int(1e9)
#
# n, m = map(int, input().split())
#
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# # x, k가 공백으로 주어짐 (거쳐갈 노드 x, 목적지 노드 k)
# x, k = map(int, input().split())
#
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# distance = graph[1][k] + graph[k][x]
#
# if distance >= INF:
#     print("-1")
# else:
#     print(distance)

##############################################################################
# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 연결되어 있다.
# 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# 도로가 연결되어 있다면 1만큼의 시간으로 이동할 수 있다.
# A는 1번 회사에서 출발하여 X번 회사를 방문한 뒤에 K번 회사로 가는 것이 목표다.
# 이때 A는 가능한 한 빠르게 이동하고자 한다. A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.


# 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M
# 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호
# M + 2번째 줄에는 X와 K
# X번 회사에 도달할 수 없다면 -1 출력

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 4번 회사를 방문한 뒤 5번 회사로 간다.

import heapq

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k를 거쳐서 x로 가는 경우
x, k = map(int, input().split())

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]
# print(distance)

if distance == INF:
    print(-1)
else:
    print(distance)

########### 다익스트라로 풀어보기
#
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 5번 회사를 방문한 뒤 4번 회사로 간다.
#
# import heapq
#
# INF = int(1e9)
# n, m = map(int, input().split())
#
# start = 1
# graph = [[] for i in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#     graph[b].append((a, 1))
#
# # 4, 5
# x, k = map(int, input().split())
# print(graph)
#
# def dijkstra(start, distance):
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
#
# distance1 = [INF] * (n + 1)
# dijkstra(1, distance1)
# print(graph)
# distance2 = [INF] * (n + 1)
# dijkstra(k, distance2)
# print(distance1)
# print(distance2)
#
# print(distance1[k] + distance2[x])
# minDistance = distance1[k] + distance2[x]
# if minDistance == INF:
#     print(-1)
# else:
#     print(minDistance)