################################# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

graph = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)

s, x, y = map(int, input().split())

print(graph)

queue = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((i, j, graph[i][j], 0))

queue.sort(key=lambda x:x[2])

queue = deque(queue)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    qx, qy, value, time = queue.popleft()

    if s == time:
        break
    for i in range(4):
        nx = qx + dx[i]
        ny = qy + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = value
                queue.append((nx, ny, graph[nx][ny], time + 1))

print(graph)
print(graph[x - 1][y - 1])
