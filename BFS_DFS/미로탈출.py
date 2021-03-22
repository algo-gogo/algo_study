# 입력받은 행렬에서 동빈이의 위치는 (1, 1) 미로의 출구는 (n, m) 괴물이 존재 0, 존재 X 1
# 괴물을 피해 탈출할 수 있는 최소 경로의 수

# 입력 : n(행), m(열)  (4<=n,m<= 200) , n X m 으로 이루어진 행렬
# 출력 : 최소 경로의 수

# BFS 사용 - 가장 인접한 부분으로 가야해서
from collections import deque

n, m = map(int, input().split())  # 행, 렬

array = []
for i in range(n):
    array.append(list(map(int, input())))  # 행렬

# 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if array[nx][ny] == 0:
#                 continue
#             if array[nx][ny] == 1:
#                 array[nx][ny] = array[x][y] + 1
#                 queue.append((nx, ny))
#     return array[n - 1][m - 1]
#
#
# print(bfs(0, 0))
###################################

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 1:
                    array[nx][ny] = array[x][y] + 1
                    queue.append((nx, ny))

    return array[n - 1][m - 1]

print(bfs(0, 0))

####################################

# from collections import deque
#
# # 오 왼 아 위
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# q = deque()
# check = [[False] * m for _ in range(n)]
# dist = [[0] * m for _ in range(n)]
#
# q.append((0, 0))
# check[0][0] = False
# dist[0][0] = 1  # 최단경로 수
#
# while q:
#     x, y = q.popleft()
#     for k in range(4):
#         nx, ny = x = dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if check[nx][ny] == False and graph[nx][ny] == 1:
#                 q.append((nx, ny))
#                 dist[nx][ny] = dist[x][y] + 1
#                 check[nx][ny] = True
#
# print(dist[n - 1][m - 1])
