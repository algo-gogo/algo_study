### BFS 문제
# 특정 도시 X 로부터 출발하여 도달할 수 있는 모든 도시 중에서 최단 거리가 정확히 k 인 도시들의 번호 출력
# 입력: 도시의 개수 N , 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
#      M개의 줄에 걸쳐서 A에서 B로 가는 단방향 도로
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
#
# from collections import deque
#
# n, m, k, x = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
# distance = [0] * (n + 1)
# visited = [False] * (n + 1)
#
# # 1, 2, 3, 4 도시에서 뻗어가는 경로
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# print(graph)
# print(distance)
# print(visited)
#
#
# # 최단거리, 출발도시
# def bfs(dist, start):
#     q = deque()
#     q.append(start)
#     answer = []
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)
#                 distance[i] = distance[i] + 1
#                 if distance[i] == dist:
#                     answer.append(i)
#
#     if len(answer) == 0:
#         print(-1)
#     else:
#         for i in answer:
#             answer.sort()
#             print(answer)
#
#     return
#
#
# bfs(k, x)


# def bfs(start):
#     answer = []
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#     distance[start] = 0
#     while queue:
#         now = queue.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#                 distance[i] = distance[now] + 1
#                 if distance[i] == k:
#                     answer.append(i)
#     if len(answer) == 0:
#         print(-1)
#     else:
#         answer.sort()
#         for i in answer:
#             print(i)


###############################

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)
print(visited)
print(distance)


def bfs(start):
    resultList = []
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    resultList.append(i)

    if len(resultList) == 0:
        print(-1)
    else:
        resultList.sort()
        for result in resultList:
            print(result)


bfs(x)
