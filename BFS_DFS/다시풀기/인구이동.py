# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, left, rignt, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    country_list = [(i, j)]
    people_num = graph[i][j]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if left <= abs(graph[x][y] - graph[nx][ny]) <= rignt:
                        visited[nx][ny] = True
                        country_list.append((nx, ny))
                        queue.append((nx, ny))
                        people_num += graph[nx][ny]

    c_p_num = people_num // len(country_list)
    for country in country_list:
        graph[country[0]][country[1]] = c_p_num
    return len(country_list), visited

queue_list = []

result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                country_list_length, visited = bfs(i, j, l, r, visited)
                if country_list_length > 1:
                    flag = True

    if not flag:
        break
    result += 1

print(result)