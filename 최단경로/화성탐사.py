import heapq
from collections import deque

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)
t = int(input())

def dijkstra(x, y, graph):
    q = []
    heapq.heappush(q, (x, y, graph[x][y]))
    distance[x][y] = graph[x][y]

    while q:
        x, y, dist = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
            else:
                continue

    return distance[len(graph) - 1][len(graph) - 1]


for _ in range(t):
    # 탐사 공간의 크기 정수 n x n
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        l = list(map(int, input().split()))
        graph.append(l)

    print(dijkstra(0, 0, graph))


# ### bfs로 풀 수 있을듯?
#
# # 상 하 좌 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x, y, array, visited):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for direction in range(4):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     array[nx][ny] = array[nx][ny] + array[x][y]
#                     queue.append((nx, ny))
#             else:
#                 continue
#
#     return array[n - 1][n - 1]
#
#
# INF = int(1e9)
# t = int(input())
#
# for _ in range(t):
#     # 탐사 공간의 크기 정수 n x n
#     n = int(input())
#     graph = []
#     visited = [[False for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         l = list(map(int, input().split()))
#         graph.append(l)
#
#     print(bfs(0, 0, graph, visited))
