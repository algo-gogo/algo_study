########################### 음료수 얼려 먹기
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def dfs(graph, x, y, n, m):
#     if 0 <= x < n and 0 <= y < m:
#         if graph[x][y] == 0:
#             graph[x][y] = 1
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 dfs(graph, nx, ny, n, m)
#             return True
#         else:
#             return False
#
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     l = list(map(int, input()))
#     graph.append(l)
#
# print(graph)
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(graph, i, j, n, m):
#             count += 1
#
# print(count)

############################ 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y, 1))
    print(queue)
    visited = [[False for _ in range(m)] for _ in range(n) ]

    print(visited)
    visited[x][y] = True
    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count + 1))


    return -1


for i in range(n):
    l = list(map(int, input()))
    graph.append(l)

result = bfs(0, 0, graph)
print(result)

