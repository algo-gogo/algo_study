# 요약
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개, 도시들이 메시지 받는 데까지 걸리는 시간

# 입력: 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C   3 2 1
# 둘째 줄부터 M + 1번 째 줄까지 X Y Z 주어짐 => X에서 다른 도시 Y 로 이어지는 통로, 메시지가 전달되는 시간 Z
# 출력: 메시지를 받는 도시의 총 개수와 총 걸리는 시간

# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m, start = map(int, input().split)
# graph = [[] for i in range(n + 1)]
#
# distance = [INF] * (n + 1)
#
# # 간선 정보 입력받기
# for _ in range(m):
#     x, y, z = map(int, input().splist())
#     graph[x].append((y, z))
#
# def dijstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijstra(start)
#
# count = 0
#
# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance, d)
#
# print(count -1, max_distance)

############################################################




# 요약
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개, 도시들이 메시지 받는 데까지 걸리는 시간
#
# 입력: 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C   3 2 1
# 둘째 줄부터 M + 1번 째 줄까지 X Y Z 주어짐 => X에서 다른 도시 Y 로 이어지는 통로, 메시지가 전달되는 시간 Z
# 출력: 메시지를 받는 도시의 총 개수와 총 걸리는 시간

# 3 2 1
# 1 2 4
# 1 3 2

# 2 4

# import heapq
#
# n, m, c = map(int, input().split())
#
# INF = int(1e9)
#
# graph = [[] for i in range(n + 1)]
# distance = [INF] * (n + 1)
#
# for i in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))
#
# def dijstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijstra(c)
#
# count = 0
#
# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance, d)
#
# print(count - 1, max_distance)

### 플로이드로 풀어보기

n, m, c = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph[c])

count = 0
resultList = []
for i in graph[c]:
    if i == INF or i == 0:
        pass
    else:
        count += 1
        resultList.append(i)

print(count, max(resultList))

